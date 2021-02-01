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
EXCEPTION_SELL_STRUCTURES_BEFORE_PROCEEDING_WITH_ACTION = 'sell_structures_before_proceeding_with_action'

# TODO: The construction of the structures must take place in a proportionate way on soils of the same color.
EXCEPTION_BUILD_STRUCTURES_PROPORTIONATE_ON_PROPERTY_GROUP = 'build_structures_proportionate_on_property_group'

# TODO: The destruction of the structures must take place in a proportionate way on soils of the same color.
EXCEPTION_DESTROY_STRUCTURES_PROPORTIONATE_ON_PROPERTY_GROUP = 'destroy_structures_proportionate_on_property_group'
