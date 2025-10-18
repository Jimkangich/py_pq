

from camel import to_snake_case


def test_camel_cased_input():
    assert to_snake_case("snakeCase") == "snake_case"
    assert to_snake_case("camelCase") == "camel_case"
    assert to_snake_case("preferredFirstName") == "preferred_first_name"
    assert to_snake_case("thatWasHorrendous") == "that_was_horrendous"
    assert to_snake_case("whichCaseDoYouPrefer") == "which_case_do_you_prefer"


def test_edge_cases_input():
    assert to_snake_case(
        "ALLCAPSWHATHEHELLY") == "_a_l_l_c_a_p_s_w_h_a_t_h_e_h_e_l_l_y"
    assert to_snake_case("goodNightJiM") == "good_night_ji_m"
    assert to_snake_case("whatADay") == "what_a_day"
