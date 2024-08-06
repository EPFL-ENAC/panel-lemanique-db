#' Apply all zaps on data frame
#'
#' \code{zap_all} applies all haven::zap_* functions except zap_empty to the data frame passed
#' as argument
#'
#' @param x Data frame
#'
#' @return Data frame
#'
zap_all <- function(x) {
  assertthat::assert_that(is.data.frame(x))

  x |>
    haven::zap_labels() |>
    haven::zap_formats() |>
    haven::zap_label() |>
    haven::zap_widths()
}

#' Assign unit name to variants
#'
#' \code{get_labels} creates a data frame with one row per question and per potential value,
#'
#' @param x Data frame
#'
#' @inheritParams rlang::args_dots_used
#'
#' @return Data frame, with columns !!names_to, name and value
get_labels <- function(x, ..., names_to = "variable_name") {

  assertthat::assert_that(is.data.frame(x))
  rlang::check_dots_empty()
  assertthat::assert_that(rlang::is_string(names_to))

  x <- x |>
    dplyr::select(tidyselect::where(haven::is.labelled))

  if (ncol(x) == 0) {
    return(tibble::tibble("{names_to}" := character(), name = character(), value = integer()))
  }

  x |>
    purrr::map(~ tibble::enframe(attr(.x, "labels"))) |>
    purrr::list_rbind(names_to = names_to)
}
