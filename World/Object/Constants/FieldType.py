from enum import Enum
from World.Object.Constants.UpdateObjectFields import ObjectField, ItemField, ContainerField, UnitField, PlayerField


class FieldType(Enum):

    INT32       = 1
    TWO_INT16   = 2
    FLOAT       = 3
    INT64       = 4
    FOUR_BYTES  = 5


FIELD_TYPE_MAP = {

    ObjectField.GUID:                       FieldType.INT64.value,
    ObjectField.TYPE:                       FieldType.INT32.value,
    ObjectField.ENTRY:                      FieldType.INT32.value,
    ObjectField.SCALE_X:                    FieldType.FLOAT.value,
    #ObjectField.PADDING:                    FieldType.INT32.value,

    ItemField.OWNER:                        FieldType.INT64.value,
    ItemField.CONTAINED:                    FieldType.INT64.value,
    ItemField.CREATOR:                      FieldType.INT64.value,
    ItemField.GIFTCREATOR:                  FieldType.INT64.value,
    ItemField.STACK_COUNT:                  FieldType.INT32.value,
    ItemField.DURATION:                     FieldType.INT32.value,
    ItemField.SPELL_CHARGES:                FieldType.INT32.value,
    ItemField.FLAGS:                        FieldType.TWO_INT16.value,
    ItemField.ENCHANTMENT:                  FieldType.INT32.value,
    ItemField.PROPERTY_SEED:                FieldType.INT32.value,
    ItemField.RANDOM_PROPERTIES_ID:         FieldType.INT32.value,
    ItemField.ITEM_TEXT_ID:                 FieldType.INT32.value,
    ItemField.DURABILITY:                   FieldType.INT32.value,
    ItemField.MAXDURABILITY:                FieldType.INT32.value,

    ContainerField.NUM_SLOTS:               FieldType.INT32.value,
    ContainerField.SLOT_1:                  FieldType.INT64.value,

    UnitField.CHARM:                        FieldType.INT64.value,
    UnitField.SUMMON:                       FieldType.INT64.value,
    UnitField.CHARMEDBY:                    FieldType.INT64.value,
    UnitField.SUMMONEDBY:                   FieldType.INT64.value,
    UnitField.CREATEDBY:                    FieldType.INT64.value,
    UnitField.TARGET:                       FieldType.INT64.value,
    UnitField.PERSUADED:                    FieldType.INT64.value,
    UnitField.CHANNEL_OBJECT:               FieldType.INT64.value,
    UnitField.HEALTH:                       FieldType.INT32.value,
    UnitField.POWER1:                       FieldType.INT32.value,
    UnitField.POWER2:                       FieldType.INT32.value,
    UnitField.POWER3:                       FieldType.INT32.value,
    UnitField.POWER4:                       FieldType.INT32.value,
    UnitField.POWER5:                       FieldType.INT32.value,
    UnitField.MAXHEALTH:                    FieldType.INT32.value,
    UnitField.MAXPOWER1:                    FieldType.INT32.value,
    UnitField.MAXPOWER2:                    FieldType.INT32.value,
    UnitField.MAXPOWER3:                    FieldType.INT32.value,
    UnitField.MAXPOWER4:                    FieldType.INT32.value,
    UnitField.MAXPOWER5:                    FieldType.INT32.value,
    UnitField.LEVEL:                        FieldType.INT32.value,
    UnitField.FACTIONTEMPLATE:              FieldType.INT32.value,
    UnitField.BYTES_0:                      FieldType.FOUR_BYTES.value,
    UnitField.VIRTUAL_ITEM_SLOT_DISPLAY:    FieldType.INT32.value,
    UnitField.VIRTUAL_ITEM_INFO:            FieldType.FOUR_BYTES.value,
    UnitField.FLAGS:                        FieldType.INT32.value,
    UnitField.FLAGS_2:                      FieldType.INT32.value,
    UnitField.AURA:                         FieldType.INT32.value,
    UnitField.AURALEVELS:                   FieldType.FOUR_BYTES.value,
    UnitField.AURAAPPLICATIONS:             FieldType.FOUR_BYTES.value,
    UnitField.AURAFLAGS:                    FieldType.FOUR_BYTES.value,
    UnitField.AURASTATE:                    FieldType.INT32.value,
    UnitField.BASEATTACKTIME:               FieldType.INT32.value,
    UnitField.OFFHANDATTACKTIME:            FieldType.INT32.value,
    UnitField.RANGEDATTACKTIME:             FieldType.INT32.value,
    UnitField.BOUNDINGRADIUS:               FieldType.FLOAT.value,
    UnitField.COMBATREACH:                  FieldType.FLOAT.value,
    UnitField.DISPLAYID:                    FieldType.INT32.value,
    UnitField.NATIVEDISPLAYID:              FieldType.INT32.value,
    UnitField.MOUNTDISPLAYID:               FieldType.INT32.value,
    UnitField.MINDAMAGE:                    FieldType.FLOAT.value,
    UnitField.MAXDAMAGE:                    FieldType.FLOAT.value,
    UnitField.MINOFFHANDDAMAGE:             FieldType.FLOAT.value,
    UnitField.MAXOFFHANDDAMAGE:             FieldType.FLOAT.value,
    UnitField.BYTES_1:                      FieldType.FOUR_BYTES.value,
    UnitField.PETNUMBER:                    FieldType.INT32.value,
    UnitField.PET_NAME_TIMESTAMP:           FieldType.INT32.value,
    UnitField.PETEXPERIENCE:                FieldType.INT32.value,
    UnitField.PETNEXTLEVELEXP:              FieldType.INT32.value,
    UnitField.DYNAMIC_FLAGS:                FieldType.INT32.value,
    UnitField.CHANNEL_SPELL:                FieldType.INT32.value,
    UnitField.MOD_CAST_SPEED:               FieldType.FLOAT.value,
    UnitField.CREATED_BY_SPELL:             FieldType.INT32.value,

    UnitField.NPC_FLAGS:                    FieldType.INT32.value,
    UnitField.NPC_EMOTESTATE:               FieldType.INT32.value,

    UnitField.TRAINING_POINTS:              FieldType.TWO_INT16.value,

    UnitField.STAT0:                        FieldType.INT32.value,
    UnitField.STAT1:                        FieldType.INT32.value,
    UnitField.STAT2:                        FieldType.INT32.value,
    UnitField.STAT3:                        FieldType.INT32.value,
    UnitField.STAT4:                        FieldType.INT32.value,
    UnitField.POSSTAT0:                     FieldType.INT32.value,
    UnitField.POSSTAT1:                     FieldType.INT32.value,
    UnitField.POSSTAT2:                     FieldType.INT32.value,
    UnitField.POSSTAT3:                     FieldType.INT32.value,
    UnitField.POSSTAT4:                     FieldType.INT32.value,
    UnitField.NEGSTAT0:                     FieldType.INT32.value,
    UnitField.NEGSTAT1:                     FieldType.INT32.value,
    UnitField.NEGSTAT2:                     FieldType.INT32.value,
    UnitField.NEGSTAT3:                     FieldType.INT32.value,
    UnitField.NEGSTAT4:                     FieldType.INT32.value,

    UnitField.RESISTANCE_NORMAL:            FieldType.INT32.value,
    UnitField.RESISTANCE_HOLY:              FieldType.INT32.value,
    UnitField.RESISTANCE_FIRE:              FieldType.INT32.value,
    UnitField.RESISTANCE_NATURE:            FieldType.INT32.value,
    UnitField.RESISTANCE_FROST:             FieldType.INT32.value,
    UnitField.RESISTANCE_SHADOW:            FieldType.INT32.value,
    UnitField.RESISTANCE_ARCANE:            FieldType.INT32.value,

    UnitField.RESISTANCE_NORMAL_BUFF_MOD_POS:       FieldType.INT32.value,
    UnitField.RESISTANCE_HOLY_BUFF_MOD_POS:         FieldType.INT32.value,
    UnitField.RESISTANCE_FIRE_BUFF_MOD_POS:         FieldType.INT32.value,
    UnitField.RESISTANCE_NATURE_BUFF_MOD_POS:       FieldType.INT32.value,
    UnitField.RESISTANCE_FROST_BUFF_MOD_POS:        FieldType.INT32.value,
    UnitField.RESISTANCE_SHADOW_BUFF_MOD_POS:       FieldType.INT32.value,
    UnitField.RESISTANCE_ARCANE_BUFF_MOD_POS:       FieldType.INT32.value,

    UnitField.RESISTANCE_NORMAL_BUFF_MOD_NEG:       FieldType.INT32.value,
    UnitField.RESISTANCE_HOLY_BUFF_MOD_NEG:         FieldType.INT32.value,
    UnitField.RESISTANCE_FIRE_BUFF_MOD_NEG:         FieldType.INT32.value,
    UnitField.RESISTANCE_NATURE_BUFF_MOD_NEG:       FieldType.INT32.value,
    UnitField.RESISTANCE_FROST_BUFF_MOD_NEG:        FieldType.INT32.value,
    UnitField.RESISTANCE_SHADOW_BUFF_MOD_NEG:       FieldType.INT32.value,
    UnitField.RESISTANCE_ARCANE_BUFF_MOD_NEG:       FieldType.INT32.value,

    UnitField.BASE_MANA:                    FieldType.INT32.value,
    UnitField.BASE_HEALTH:                  FieldType.INT32.value,
    UnitField.BYTES_2:                      FieldType.FOUR_BYTES.value,
    UnitField.ATTACK_POWER:                 FieldType.INT32.value,
    UnitField.ATTACK_POWER_MODS:            FieldType.TWO_INT16.value,
    UnitField.ATTACK_POWER_MULTIPLIER:      FieldType.FLOAT.value,
    UnitField.RANGED_ATTACK_POWER:          FieldType.INT32.value,
    UnitField.RANGED_ATTACK_POWER_MODS:     FieldType.TWO_INT16.value,
    UnitField.RANGED_ATTACK_POWER_MULTIPLIER:     FieldType.FLOAT.value,
    UnitField.MINRANGEDDAMAGE:              FieldType.FLOAT.value,
    UnitField.MAXRANGEDDAMAGE:              FieldType.FLOAT.value,
    UnitField.POWER_COST_MODIFIER:          FieldType.INT32.value,
    UnitField.POWER_COST_MULTIPLIER:        FieldType.FLOAT.value,
    UnitField.MAXHEALTHMODIFIER:            FieldType.FLOAT.value,
    #UnitField.PADDING:                      FieldType.INT32.value,

    PlayerField.DUEL_ARBITER:               FieldType.INT64.value,
    PlayerField.FLAGS:                      FieldType.INT32.value,
    PlayerField.GUILDID:                    FieldType.INT32.value,
    PlayerField.GUILDRANK:                  FieldType.INT32.value,

    PlayerField.BYTES_1:                    FieldType.FOUR_BYTES.value,
    PlayerField.BYTES_2:                    FieldType.FOUR_BYTES.value,
    PlayerField.BYTES_3:                    FieldType.FOUR_BYTES.value,

    PlayerField.DUEL_TEAM:                  FieldType.INT32.value,
    PlayerField.GUILD_TIMESTAMP:            FieldType.INT32.value,

    PlayerField.QUEST_LOG_1_1:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_1_2:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_1_3:              FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_1_4:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_2_1:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_2_2:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_2_3:              FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_2_4:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_3_1:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_3_2:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_3_3:              FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_3_4:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_4_1:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_4_2:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_4_3:              FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_4_4:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_5_1:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_5_2:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_5_3:              FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_5_4:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_6_1:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_6_2:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_6_3:              FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_6_4:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_7_1:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_7_2:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_7_3:              FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_7_4:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_8_1:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_8_2:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_8_3:              FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_8_4:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_9_1:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_9_2:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_9_3:              FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_9_4:              FieldType.INT32.value,
    PlayerField.QUEST_LOG_10_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_10_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_10_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_10_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_11_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_11_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_11_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_11_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_12_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_12_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_12_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_12_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_13_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_13_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_13_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_13_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_14_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_14_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_14_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_14_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_15_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_15_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_15_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_15_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_16_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_16_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_16_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_16_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_17_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_17_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_17_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_17_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_18_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_18_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_18_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_18_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_19_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_19_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_19_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_19_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_20_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_20_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_20_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_20_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_21_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_21_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_21_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_21_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_22_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_22_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_22_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_22_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_23_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_23_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_23_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_23_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_24_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_24_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_24_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_24_4:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_25_1:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_25_2:             FieldType.INT32.value,
    PlayerField.QUEST_LOG_25_3:             FieldType.FOUR_BYTES.value,
    PlayerField.QUEST_LOG_25_4:             FieldType.INT32.value,

    PlayerField.VISIBLE_ITEM_1_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_1_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_1_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_1_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_2_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_2_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_2_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_2_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_3_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_3_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_3_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_3_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_4_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_4_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_4_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_4_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_5_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_5_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_5_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_5_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_6_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_6_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_6_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_6_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_7_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_7_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_7_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_7_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_8_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_8_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_8_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_8_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_9_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_9_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_9_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_9_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_10_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_10_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_10_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_10_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_11_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_11_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_11_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_11_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_12_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_12_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_12_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_12_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_13_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_13_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_13_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_13_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_14_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_14_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_14_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_14_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_15_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_15_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_15_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_15_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_16_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_16_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_16_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_16_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_17_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_17_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_17_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_17_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_18_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_18_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_18_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_18_PAD:         FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_19_CREATOR:     FieldType.INT64.value,
    PlayerField.VISIBLE_ITEM_19_0:           FieldType.INT32.value,
    PlayerField.VISIBLE_ITEM_19_PROPERTIES:  FieldType.TWO_INT16.value,
    PlayerField.VISIBLE_ITEM_19_PAD:         FieldType.INT32.value,

    PlayerField.CHOSEN_TITLE:               FieldType.INT32.value,
    PlayerField.PAD_0:                      FieldType.INT32.value,
    PlayerField.INV_SLOT_HEAD:              FieldType.INT64.value,
    PlayerField.INV_SLOT_NECK:              FieldType.INT64.value,
    PlayerField.INV_SLOT_SHOULDERS:         FieldType.INT64.value,
    PlayerField.INV_SLOT_BODY:              FieldType.INT64.value,
    PlayerField.INV_SLOT_CHEST:             FieldType.INT64.value,
    PlayerField.INV_SLOT_WAIST:             FieldType.INT64.value,
    PlayerField.INV_SLOT_LEGS:              FieldType.INT64.value,
    PlayerField.INV_SLOT_FEET:              FieldType.INT64.value,
    PlayerField.INV_SLOT_WRISTS:            FieldType.INT64.value,
    PlayerField.INV_SLOT_HANDS:             FieldType.INT64.value,
    PlayerField.INV_SLOT_FINGER1:           FieldType.INT64.value,
    PlayerField.INV_SLOT_FINGER2:           FieldType.INT64.value,
    PlayerField.INV_SLOT_TRINKET1:          FieldType.INT64.value,
    PlayerField.INV_SLOT_TRINKET2:          FieldType.INT64.value,
    PlayerField.INV_SLOT_BACK:              FieldType.INT64.value,
    PlayerField.INV_SLOT_MAINHAND:          FieldType.INT64.value,
    PlayerField.INV_SLOT_OFFHAND:           FieldType.INT64.value,
    PlayerField.INV_SLOT_RANGED:            FieldType.INT64.value,
    PlayerField.INV_SLOT_TABARD:            FieldType.INT64.value,
    PlayerField.INV_SLOT_BAG1:              FieldType.INT64.value,
    PlayerField.INV_SLOT_BAG2:              FieldType.INT64.value,
    PlayerField.INV_SLOT_BAG3:              FieldType.INT64.value,
    PlayerField.INV_SLOT_BAG4:              FieldType.INT64.value,

    PlayerField.PACK_SLOT_1:                FieldType.INT64.value,
    PlayerField.BANK_SLOT_1:                FieldType.INT64.value,
    PlayerField.BANKBAG_SLOT_1:             FieldType.INT64.value,
    PlayerField.VENDORBUYBACK_SLOT_1:       FieldType.INT64.value,
    PlayerField.KEYRING_SLOT_1:             FieldType.INT64.value,
    PlayerField.VANITYPET_SLOT_1:           FieldType.INT64.value,

    PlayerField.FARSIGHT:                   FieldType.INT64.value,
    PlayerField._FIELD_KNOWN_TITLES:        FieldType.INT64.value,

    PlayerField.XP:                         FieldType.INT32.value,
    PlayerField.NEXT_LEVEL_XP:              FieldType.INT32.value,

    PlayerField.SKILL_INFO_1_ID:            FieldType.INT32.value,
    PlayerField.SKILL_INFO_1_LEVEL:         FieldType.INT32.value,
    PlayerField.SKILL_INFO_1_STAT_LEVEL:    FieldType.INT32.value,
    PlayerField.CHARACTER_POINTS1:          FieldType.INT32.value,
    PlayerField.CHARACTER_POINTS2:          FieldType.INT32.value,
    PlayerField.TRACK_CREATURES:            FieldType.INT32.value,
    PlayerField.TRACK_RESOURCES:            FieldType.INT32.value,
    PlayerField.BLOCK_PERCENTAGE:           FieldType.FLOAT.value,
    PlayerField.DODGE_PERCENTAGE:           FieldType.FLOAT.value,
    PlayerField.PARRY_PERCENTAGE:           FieldType.FLOAT.value,
    PlayerField.EXPERTISE:                  FieldType.INT32.value,
    PlayerField.OFFHAND_EXPERTISE:          FieldType.INT32.value,
    PlayerField.CRIT_PERCENTAGE:            FieldType.FLOAT.value,
    PlayerField.RANGED_CRIT_PERCENTAGE:     FieldType.FLOAT.value,
    PlayerField.OFFHAND_CRIT_PERCENTAGE:    FieldType.FLOAT.value,

    PlayerField.SPELL_CRIT_NORMAL_PERCENTAGE:   FieldType.FLOAT.value,
    PlayerField.SPELL_CRIT_HOLY_PERCENTAGE:     FieldType.FLOAT.value,
    PlayerField.SPELL_CRIT_FIRE_PERCENTAGE:     FieldType.FLOAT.value,
    PlayerField.SPELL_CRIT_NATURE_PERCENTAGE:   FieldType.FLOAT.value,
    PlayerField.SPELL_CRIT_FROST_PERCENTAGE:    FieldType.FLOAT.value,
    PlayerField.SPELL_CRIT_SHADOW_PERCENTAGE:   FieldType.FLOAT.value,
    PlayerField.SPELL_CRIT_ARCANE_PERCENTAGE:   FieldType.FLOAT.value,

    PlayerField.SHIELD_BLOCK:               FieldType.INT32.value,
    PlayerField.EXPLORED_ZONES_1:           FieldType.FOUR_BYTES.value,
    PlayerField.REST_STATE_EXPERIENCE:      FieldType.INT32.value,
    PlayerField.COINAGE:                      FieldType.INT32.value,

    # PlayerField.MOD_DAMAGE_0_DONE_POS:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_1_DONE_POS:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_2_DONE_POS:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_3_DONE_POS:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_4_DONE_POS:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_5_DONE_POS:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_6_DONE_POS:      FieldType.INT32.value,
    #
    # PlayerField.MOD_DAMAGE_0_DONE_NEG:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_1_DONE_NEG:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_2_DONE_NEG:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_3_DONE_NEG:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_4_DONE_NEG:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_5_DONE_NEG:      FieldType.INT32.value,
    # PlayerField.MOD_DAMAGE_6_DONE_NEG:      FieldType.INT32.value,
    #
    PlayerField.MOD_DAMAGE_NORMAL_DONE_PCT:      FieldType.INT32.value,
    PlayerField.MOD_DAMAGE_HOLY_DONE_PCT:      FieldType.INT32.value,
    PlayerField.MOD_DAMAGE_FIRE_DONE_PCT:      FieldType.INT32.value,
    PlayerField.MOD_DAMAGE_NATURE_DONE_PCT:      FieldType.INT32.value,
    PlayerField.MOD_DAMAGE_FROST_DONE_PCT:      FieldType.INT32.value,
    PlayerField.MOD_DAMAGE_SHADOW_DONE_PCT:      FieldType.INT32.value,
    PlayerField.MOD_DAMAGE_ARCANE_DONE_PCT:      FieldType.INT32.value,

    PlayerField.BYTES:                        FieldType.FOUR_BYTES.value,
    PlayerField.WATCHED_FACTION_INDEX:        FieldType.INT32.value,
    # PlayerField.AMMO_ID:                    FieldType.INT32.value,
    # PlayerField.PVP_MEDALS:                 FieldType.INT32.value,
    # PlayerField.BUYBACK_ITEM_ID:            FieldType.INT32.value,
    # PlayerField.BUYBACK_RANDOM_PROP_ID:     FieldType.INT32.value,
    # PlayerField.BUYBACK_SEED:               FieldType.INT32.value,
    # PlayerField.BUYBACK_PRICE:              FieldType.INT32.value
    PlayerField.MAX_LEVEL:                      FieldType.INT32.value
}

# TODO: 128 should be moved to constants or replaced with Player.NUM_SKILLS
for i in range(128):
    FIELD_TYPE_MAP.update({
        PlayerField.SKILL_INFO_1_ID.value + i*3:         FieldType.INT32,
        PlayerField.SKILL_INFO_1_LEVEL.value + i*3:      FieldType.INT32,
        PlayerField.SKILL_INFO_1_STAT_LEVEL.value + i*3: FieldType.INT32
    })