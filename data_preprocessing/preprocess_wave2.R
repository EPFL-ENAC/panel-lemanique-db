here::i_am("./preprocess_wave2.R")

source(here::here("utils.R"))

folder <- "/Volumes/LASUR/common/LaSUR/06 - Recherche/Dossier de travail IT4R/"

wave2_data <- haven::read_sav(
  file.path(
    folder,
    "Enquête consommation/Data/Database from FORS/EPFL Panel LÇmanique Vague 2 _FINAL_EPFL.sav"
  )
)

names(wave2_data) <- janitor::make_clean_names(names(wave2_data), case = "snake", ascii = TRUE)

participants_colnames <- c(
  "idno", "pays", "groupe", "gp_age_source", "insee", "ofs", "weight", "titre_source", "cp_source",
  "localite_source"
)

survey_metadata_colnames <- c(
  "countmiss1", "countmiss2", "progress", "start_date", "end_date", "temps_minute"
)

# TODO: figure out with Panel team what to do with these additional variables.
extra_colnames <- c(
  "titre_actuel", "cp_actuel", "localite_actuel", "code_raison_contact_1_v2",
  "code_raison_contact_2_v2", "code_raison_contact_3_v2", "particip_avant_changements",
  "flag_troll", "particip_v2", "suppression_suite_v2", "flag_chgmt_pays", "mobile_ordi",
  "avant_chgmt_vet", "flag_chgmt_localite_v2"
)

# Clean-up questions
questions <- wave2_data |>
  dplyr::select(
    -tidyselect::all_of(participants_colnames),
    -tidyselect::all_of(survey_metadata_colnames),
    -tidyselect::all_of(extra_colnames)
  )

question_labels <- get_labels(questions, names_to = "question_code")

questions <- questions |>
  purrr::map(~ attr(.x, "label")) |>
  unlist() |>
  tibble::enframe(name = "question_code", value = "question_text")

questions <- questions |>
  dplyr::mutate(section_name = stringr::str_extract(question_code, "^[:alpha:]+(?=\\_)")) |>
  dplyr::mutate(section_name = dplyr::case_match(
    section_name,
    "ali" ~ "Alimentation",
    "con" ~ "Consommation",
    "end" ~ "Satisfaction",
    "ene" ~ "Energie",
    "equ" ~ "Equipement",
    "log" ~ "Logement",
    "rep" ~ "Rep",
    "temp" ~ "Temperature",
    "vot" ~ "Votation"
  ))

# Need to create the survey and section IDs when these are added to the database, somehow
sections <- questions |>
  dplyr::select(section_name) |>
  dplyr::group_by(section_name) |>
  dplyr::slice_head(n = 1) |>
  dplyr::ungroup()

questions <- questions |>
  dplyr::left_join(sections, by = "section_name") |>
  dplyr::select(-section_name)

# Clean-up participants

participants <- wave2_data |>
  dplyr::select(tidyselect::all_of(participants_colnames)) |>
  dplyr::rename(numero_insee = insee, numero_ofs = ofs)

participant_labels <- get_labels(participants)

participants <- participants |>
  zap_all() |>
  dplyr::mutate(numero_insee = strtoi(numero_insee, base = 10L))

# Clean-up surveys
survey_completion <- wave2_data |>
  dplyr::select(
    idno, countmiss1, countmiss2, progress, start_date, end_date, temps_minute, flag_troll
  )

survey_completion_labels <- get_labels(survey_completion)

survey_completion <- survey_completion |>
  zap_all()

# Write everything to file
output_folder <- "data/wave2"

if (!dir.exists(here::here(output_folder))) {
  dir.create(here::here(output_folder), recursive = TRUE)
}

output_folder <- here::here(output_folder)

readr::write_tsv(participant_labels, here::here(output_folder, "participant_labels.tsv"))
readr::write_tsv(participants, here::here(output_folder, "participants.tsv"))
readr::write_tsv(question_labels, here::here(output_folder, "question_labels.tsv"))
readr::write_tsv(questions, here::here(output_folder, "questions.tsv"))
readr::write_tsv(sections, here::here(output_folder, "sections.tsv"))
readr::write_tsv(survey_completion, here::here(output_folder, "survey_completion.tsv"))
readr::write_tsv(
  survey_completion_labels, here::here(output_folder, "survey_completion_labels.tsv")
)
