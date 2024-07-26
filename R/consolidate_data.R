library(dplyr)
library(haven)

folder <- "/Volumes/LASUR/common/LaSUR/06 - Recherche/Dossier de travail IT4R/"

############################### Wave 1 ###############################

wave1_data <- haven::read_sav(
  file.path(
    folder,
    "Enquête mobilité/EPFL_vague1_pond_clean_240319.sav"
  )
)

wave1_data <- wave1_data |>
  haven::zap_labels()

############################### Wave 2 ###############################

wave2_data <- haven::read_sav(
  file.path(
    folder,
    "Enquête consommation/Data/Database from FORS/EPFL Panel LÇmanique Vague 2 _FINAL_EPFL.sav"
  )
)

wave2_data <- wave2_data |>
  haven::zap_labels()

# Add the necessary w
wave2_data <- wave2_data |>
  dplyr::left_join(
    dplyr::select(wave1_data, IDNO, wgt_agg_trim, wgt_agg_trim_v2, wgt_cant_trim, wgt_cant_trim_v2),
    by = "IDNO"
  )

# Check that wave2_data contains the same columns as the CSV file from FORS
fors_csv_data <- readr::read_csv2(
  file.path(
    folder,
    "Enquête consommation/Data/Database from FORS/EPFL Panel LÇmanique Vague 2 _FINAL_EPFL.csv"
  ),
  locale = readr::locale(encoding = "latin1"),
  show_col_types = FALSE,
  progress = FALSE
)[, -1]

assertthat::assert_that(setequal(colnames(fors_csv_data), colnames(wave2_data)))

# Add a variable that allows user to return to the CSV data
# This is equivalent to Particip_v2 %in% c(1,2)
fors_csv_data <- fors_csv_data |>
  dplyr::mutate(fors_csv = TRUE)

wave2_data <- wave2_data |>
  dplyr::left_join(
    dplyr::select(fors_csv_data, IDNO, fors_csv),
    by = "IDNO"
  ) |>
  dplyr::mutate(fors_csv = !is.na(fors_csv))

### HERUS files
# The HERUS data is a subset of participants with a complete participation (Particip_v2).
# It's unclear how exactly this subset is created
herus_rds_data <- readRDS(
  file.path(
    folder,
    "Enquête consommation/Data/Database update for report/EPFL Panel LÇmanique Vague 2 _Update_HERUS.rds"
  )
) |>
  tibble::as_tibble() |>
  dplyr::mutate(herus_rds = TRUE)

wave2_data <- wave2_data |>
  dplyr::left_join(
    dplyr::select(
      herus_rds_data, IDNO, HS_ZONE_C, HS_URBANAREA_C, weight_tot, Pays_cor, Groupe2, Groupe3, herus_rds
    ),
    by = "IDNO"
  )

############################### Post-processing ###############################

# Keep for later
names(wave1_data) <- janitor::make_clean_names(names(wave1_data), case = "snake", ascii = TRUE)

wave1_data <- wave1_data |>
  dplyr::select(-c(wgt_agg_trim_v2, wgt_cant_trim_v2))

names(wave2_data) <- janitor::make_clean_names(names(wave2_data), case = "snake", ascii = TRUE)

wave2_data <- wave2_data |>
  dplyr::select(-c(wgt_agg_trim, wgt_cant_trim))

# Check constant variables across waves
w1 <- wave1_data |> dplyr::inner_join(wave2_data |> dplyr::select(idno)) |> dplyr::arrange(idno)
w2 <- wave2_data |> dplyr::inner_join(wave1_data |> dplyr::select(idno)) |> dplyr::arrange(idno)

# The INSEE are constant across both waves (makes sense) but are stored under different variables, #
# and are stored as characters in the second wave
table(w1$numero_insee == strtoi(w2$insee, base = 10L), useNA = "ifany")
table(w1$numero_ofs == w2$ofs, useNA = "ifany")

# gp_age_source is also constant across waves
table(w1$gp_age_source, w2$gp_age_source)

# The post code is not constant across waves, somehow
inds <- which(w1$cp_source != w2$cp_source)

# Write constant data to file
constant_w1 <- wave1_data |>
  dplyr::select(idno, numero_insee, numero_ofs, groupe, gp_age_source) |>
  dplyr::arrange(idno)

constant_w2 <- wave2_data |>
  dplyr::select(idno, insee, ofs, groupe, gp_age_source) |>
  dplyr::mutate(numero_insee = strtoi(insee, base = 10L), .keep = "unused") |>
  dplyr::rename(numero_ofs = ofs) |>
  dplyr::arrange(idno)

constant_data <- constant_w1 |>
  dplyr::bind_rows(constant_w2 |> dplyr::filter(!(idno %in% constant_w1$idno)))

readr::write_tsv(constant_data, "data/constant_data.tsv")

# Quick function to trim left and right white space, as well as remove weird characters.
clean_text_data <- function(x) {
  x |>
    dplyr::mutate(dplyr::across(
      tidyselect::where(is.character),
      trimws
    )) |>
    dplyr::mutate(dplyr::across(
      tidyselect::where(is.character),
      ~ stringr::str_remove_all(.x, "[\n\r]")
    )) |>
    dplyr::mutate(dplyr::across(
      tidyselect::where(is.character),
      ~ stringr::str_remove_all(.x, "'$")
    ))
}

# Write clean wave 1 data to file
wave1_data <- wave1_data |>
  dplyr::select(-c(numero_insee, numero_ofs, groupe, gp_age_source))

wave1_data <- clean_text_data(wave1_data)

readr::write_delim(wave1_data, "data/wave1.csv", delim = ";")

# Write clean wave 1 data to file
wave2_data <- wave2_data |>
  dplyr::select(-c(insee, ofs, groupe, gp_age_source))

wave2_data <- clean_text_data(wave2_data)

readr::write_tsv(wave1_data, "data/wave2.tsv")
