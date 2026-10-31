from django.utils.translation import gettext_lazy as _

# English stable codes; Italian labels in locale/it.
IQ_GROUP = (
    ("", ""),
    ("pastry_sheet", _("Pastry sheet")),
    ("broth", _("Broth")),
    ("shortcrust", _("Shortcrust")),
    ("base", _("Base")),
    ("soak", _("Soak")),
    ("filling", _("Filling")),
    ("marinade", _("Marinade")),
    ("cream", _("Cream")),
    ("bechamel", _("Béchamel")),
    ("topping", _("Topping")),
    ("decoration", _("Decoration")),
    ("glaze", _("Glaze")),
    ("preferment", _("Preferment")),
    ("mash", _("Mash")),
    ("biga", _("Biga")),
    ("dough", _("Dough")),
    ("first_dough", _("First dough")),
    ("second_dough", _("Second dough")),
    ("frying", _("Frying")),
)

IQ_UNIT = (
    ("", ""),
    ("g", "g"),
    ("Kg", "Kg"),
    ("mL", "mL"),
    ("L", "L"),
    ("rib", _("Rib")),
    ("ribs", _("Ribs")),
    ("pinch", _("Pinch")),
    ("pinches", _("Pinches")),
    ("sachet", _("Sachet")),
    ("sachets", _("Sachets")),
    ("cube", _("Cube")),
    ("cubes", _("Cubes")),
    ("tablespoon", _("Tablespoon")),
    ("tablespoons", _("Tablespoons")),
    ("teaspoon", _("Teaspoon")),
    ("teaspoons", _("Teaspoons")),
    ("cup", _("Cup")),
    ("cups", _("Cups")),
    ("small_cup", _("Small cup")),
    ("small_cups", _("Small cups")),
    ("glass", _("Glass")),
    ("glasses", _("Glasses")),
    ("clove", _("Clove")),
    ("cloves", _("Cloves")),
    ("sprig", _("Sprig")),
    ("sprigs", _("Sprigs")),
    ("leaf", _("Leaf")),
    ("leaves", _("Leaves")),
    ("jar", _("Jar")),
    ("jars", _("Jars")),
    ("slice", _("Slice")),
    ("slices", _("Slices")),
    ("stick", _("Stick")),
    ("sticks", _("Sticks")),
)

# Approximate gram conversions for common household units (reference).
IQU_EGG_LARGE = 68
IQU_EGG = 58
IQU_EGG_WHITE = 33
IQU_EGG_YOLK = 18
IQU_RIB = 50
IQU_PINCH = 1
IQU_SACHET = 16
IQU_CUBE = 25
IQU_TABLESPOON = 25
IQU_TEASPOON = 10
IQU_CUP = 250
IQU_SMALL_CUP = 75
IQU_GLASS = 200
IQU_CLOVE = 10
IQU_SPRIG = 5
IQU_LEAF = 1
IQU_JAR = 125
IQU_SLICE = 50
IQU_STICK = 15
