# Minecraft Java Edition 1.12.2 or earlier
# Connection and blockID : MCPI
# World parameters : MCJE

print("param_MCJE1122 loaded")

# axis parameters for MCJE
AXIS_WIDTH = 40       # x, z: -40 .. 0 .. 40
AXIS_TOP = 127
AXIS_Y_V_ORG = 96     # y of virtual origin
AXIS_BOTTOM = 63      # y: 63 .. 96 .. 127

# virtical levels for MCJE
Y_TOP = 255           # the top where blocks can be set
Y_CLOUD_BOTTOM = 128  # the bottom of clouds
Y_SEA = 62            # the sea level
Y_BOTTOM = 0          # the bottom where blocks can be set
Y_BOTTOM_STEVE = -64  # the bottom where Steve can go down

# connection port for MCPI
PORT_MC = 4711

# block IDs for MCPI  ## see block.py
AIR = 0
STONE = 1
GRASS_BLOCK = 2
GOLD_BLOCK = 41
IRON_BLOCK = 42
GLOWSTONE = 89
SEA_LANTERN_BLOCK = 169  # not available in MCPI

# some good blocks for grid like patterns you can count blocks easily
GLASS = 20
TNT = 46
DIAMOND_BLOCK = 57
FURNACE_INACTIVE = 61
FURNACE_ACTIVE = 62
GLASS_PANE = 102
STONE_CUTTER = 245
GLOWING_OBSIDIAN = 246
NETHER_REACTOR_CORE = 247

LEAVES2 = 161
EMERALD_BLOCK = 133
FIRE = 51
YELLOW_FLOWER = 37
LAPIS_BLOCK = 22
LOG = 17
DIRT = 3
SAPLING = 6

BRICK_BLOCK = 45
REDSTONE_WIRE = 55
QUARTZ_BLOCK = 155
STAINED_HARDENED_CLAY = 159
PRISMARINE = 168
YELLOW_GLAZED_TERRACOTTA = 239
FLOWING_WATER = 8
STILL_WATER = 9
FLOWING_LAVA = 10
