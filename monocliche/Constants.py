# List of constants representing the error labels, in order to manage errors in multiple languages.

EXCEPTION_LABEL_BASE_PATH = 'label.exception.'

# TODO:  f"It is not possible to build more than {Region.MAXIMUM_NUMBER_OF_CONSTRUCTIONS} structures."
EXCEPTION_MAXIMUM_CONSTRUCTION_LIMIT = EXCEPTION_LABEL_BASE_PATH + 'maximum_construction_limit'

# TODO: "You don't own all the properties"
EXCEPTION_NOT_OWN_ALL_THE_PROPERTY_OF_GROUP = EXCEPTION_LABEL_BASE_PATH + 'not_own_all_the_property_of_group'

# TODO: "You cannot build on a mortgaged property."
EXCEPTION_NOT_POSSIBLE_TO_BUILD_ON_MORTGAGE_PROPERTY = EXCEPTION_LABEL_BASE_PATH + 'not_possible_to_build_on_mortgage_property'

# TODO: "It is not possible to destroy a structure from a mortgaged property."
EXCEPTION_NOT_POSSIBLE_TO_DESTROY_ON_MORTGAGE_PROPERTY = EXCEPTION_LABEL_BASE_PATH + 'not_possible_to_destroy_on_mortgage_property'

# TODO: "It is not possible to destroy properties if they no longer exist."
EXCEPTION_NO_PROPERTIES_TO_DESTROY = EXCEPTION_LABEL_BASE_PATH + 'no_properties_to_destroy'

# TODO: "Not enough money to carry out the operation."
EXCEPTION_NOT_ENOUGH_MONEY = EXCEPTION_LABEL_BASE_PATH + 'not_enough_money'

# TODO: you cannot do this on this type of property
EXCEPTION_PROPERTY_TYPE_NOT_SUPPORT_THE_ACTION = EXCEPTION_LABEL_BASE_PATH + 'property_type_not_support_the_action'

# TODO: "The property is already mortgaged."
EXCEPTION_PROPERTY_ALREADY_MORTGAGED = EXCEPTION_LABEL_BASE_PATH + 'property_already_mortgaged'

# TODO:"The property is not mortgaged"
EXCEPTION_PROPERTY_NOT_MORTGAGED = EXCEPTION_LABEL_BASE_PATH + 'property_not_mortgaged'

# TODO: "The game has already started"
EXCEPTION_GAME_ALREADY_STARTED = EXCEPTION_LABEL_BASE_PATH + 'game_already_started'

# TODO: "The game is already over"
EXCEPTION_GAME_ALREADY_OVER = EXCEPTION_LABEL_BASE_PATH + 'game_already_over'

# TODO: no player present
EXCEPTION_NO_PLAYER_PRESENT = EXCEPTION_LABEL_BASE_PATH + 'no_player_present'

# TODO: "It is not possible to leave a game that has already started"
EXCEPTION_CANNOT_LEAVE_GAME_ALREADY_STARTED = EXCEPTION_LABEL_BASE_PATH + 'cannot_leave_game_already_started'

# TODO: Structures must be removed before proceeding with this operation
EXCEPTION_SELL_STRUCTURES_BEFORE_PROCEEDING_WITH_ACTION = EXCEPTION_LABEL_BASE_PATH + 'sell_structures_before_proceeding_with_action'

# TODO: The construction of the structures must take place in a proportionate way on soils of the same color.
EXCEPTION_BUILD_STRUCTURES_PROPORTIONATE_ON_PROPERTY_GROUP = EXCEPTION_LABEL_BASE_PATH + 'build_structures_proportionate_on_property_group'

# TODO: The destruction of the structures must take place in a proportionate way on soils of the same color.
EXCEPTION_DESTROY_STRUCTURES_PROPORTIONATE_ON_PROPERTY_GROUP = EXCEPTION_LABEL_BASE_PATH + 'destroy_structures_proportionate_on_property_group'

# TODO: The target box type is invalid
EXCEPTION_BOX_TYPE_NOT_VALID = EXCEPTION_LABEL_BASE_PATH + 'box_type_not_valid'

# TODO : The destination box not exists
EXCEPTION_DESTINATION_BOX_NOT_EXISTS = EXCEPTION_LABEL_BASE_PATH + 'destination_box_not_exists'

# Number of spaces on the game board
NUMBER_OF_BOXES = 40

# Indicate the position of the prison in the list of boxes. The index is 0 based
PRISON_CELL_LOCATION = 10

# BOX NAMES
"""
Structure example

{
    label: {
                box_name: {
                            go_box: 'GO',
                            community_chest_box: 'Community chest'
                            chance_box: 'Chance'
                }
    }
}
"""

# In the name of the constants we use the name of the squares taken from the board of the English monopoly.
BASE_PATH_LABEL_BOX_NAME = 'label.box_name.'

NAME_GO_BOX = BASE_PATH_LABEL_BOX_NAME + 'go_box'
NAME_COMMUNITY_CHEST_BOX = BASE_PATH_LABEL_BOX_NAME + 'community_chest_box'
NAME_CHANCE_BOX = BASE_PATH_LABEL_BOX_NAME + 'chance_box'
NAME_SUPER_TAX_BOX = BASE_PATH_LABEL_BOX_NAME + 'super_tax_box'
NAME_FREE_PARKING_BOX = BASE_PATH_LABEL_BOX_NAME + 'free_parking_box'
NAME_JUST_VISITING_BOX = BASE_PATH_LABEL_BOX_NAME + 'just_visiting_box'
NAME_GO_TO_JAIL_BOX = BASE_PATH_LABEL_BOX_NAME + 'go_to_jail_box'
NAME_INCOME_TAX_BOX = BASE_PATH_LABEL_BOX_NAME + 'income_tax_box'
NAME_KING_CROSS_STATION_BOX = BASE_PATH_LABEL_BOX_NAME + 'king_cross_station_box'
NAME_MARYLEBONE_STATION_BOX = BASE_PATH_LABEL_BOX_NAME + 'marylebone_station_box'
NAME_FENCHURCH_STATION_BOX = BASE_PATH_LABEL_BOX_NAME + 'fenchurch_station_box'
NAME_LIVERPOOL_STATION_BOX = BASE_PATH_LABEL_BOX_NAME + 'liverpool_station_box'
NAME_ELECTRIC_COMPANY_BOX = BASE_PATH_LABEL_BOX_NAME + 'electric_company_box'
NAME_WATER_WORKS_BOX = BASE_PATH_LABEL_BOX_NAME + 'water_works_box'
NAME_OLD_KENT_ROAD_BOX = BASE_PATH_LABEL_BOX_NAME + 'old_kent_road_box'
NAME_WHITECHAPEL_ROAD_BOX = BASE_PATH_LABEL_BOX_NAME + 'whitechapel_box'
NAME_THE_ANGEL_ISLINGTON_BOX = BASE_PATH_LABEL_BOX_NAME + 'the_angel_islington_box'
NAME_EUSTON_ROAD_BOX = BASE_PATH_LABEL_BOX_NAME + 'euston_road_box'
NAME_PENTONVILLE_ROAD_BOX = BASE_PATH_LABEL_BOX_NAME + 'pentonville_road'
NAME_PALL_MALL_BOX = BASE_PATH_LABEL_BOX_NAME + 'pall_mall_box'
NAME_WHITEHALL_BOX = BASE_PATH_LABEL_BOX_NAME + 'whitehall_box'
NAME_NORTHUMRLD_AVENUE_BOX = BASE_PATH_LABEL_BOX_NAME + 'northumrld_avenue_box'
NAME_BOW_STREET_BOX = BASE_PATH_LABEL_BOX_NAME + 'bow_street_box'
NAME_MARLBOROUGH_STREET_BOX = BASE_PATH_LABEL_BOX_NAME + 'marlborough_street_box'
NAME_VINE_STREET_BOX = BASE_PATH_LABEL_BOX_NAME + 'vine_street_box'
NAME_STRAND_BOX = BASE_PATH_LABEL_BOX_NAME + 'strand_box'
NAME_FLEET_STREET_BOX = BASE_PATH_LABEL_BOX_NAME + 'fleet_street_box'
NAME_TRAFALGAR_SQUARE_BOX = BASE_PATH_LABEL_BOX_NAME + 'trafalgar_square_box'
NAME_LEICESTER_SQUARE_BOX = BASE_PATH_LABEL_BOX_NAME + 'leicester_square_box'
NAME_COVENTRY_STREET_BOX = BASE_PATH_LABEL_BOX_NAME + 'coventry_box'
NAME_PICCADILLY_BOX = BASE_PATH_LABEL_BOX_NAME + 'piccadilly_box'
NAME_REGENT_STREET_BOX = BASE_PATH_LABEL_BOX_NAME + 'regent_street_box'
NAME_OXFORD_STREET_BOX = BASE_PATH_LABEL_BOX_NAME + 'oxford_street_box'
NAME_BOND_STREET_BOX = BASE_PATH_LABEL_BOX_NAME + 'bond_street_box'
NAME_PARK_LANE_BOX = BASE_PATH_LABEL_BOX_NAME + 'park_lane_box'
NAME_MAYFAIR_BOX = BASE_PATH_LABEL_BOX_NAME + 'mayfair_box'

