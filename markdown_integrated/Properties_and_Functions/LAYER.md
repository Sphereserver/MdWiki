The layers are defined in the sphere_defs.scp file.

# Paperdoll

|  |  |  |
|----|----|----|
| **Layer ID** | **Default Layer Defname** | **Description** |
| 1 | layer_hand1 |  |
| 2 | layer_hand2 |  |
| 3 | layer_shoes |  |
| 4 | layer_pants | bone legs + pants |
| 5 | layer_shirt |  |
| 6 | layer_helm |  |
| 7 | layer_gloves |  |
| 8 | layer_ring |  |
| 9 | layer_talisman | talisman (se and ml) |
| 10 | layer_collar | gorget or necklace |
| 11 | layer_hair |  |
| 12 | layer_half_apron |  |
| 13 | layer_chest | armor chest |
| 14 | layer_wrist | watch |
| 15 | layer_light | a itemid_light_src equip item can be put here |
| 16 | layer_beard |  |
| 17 | layer_tunic | jester suit or full apron |
| 18 | layer_ears | earrings |
| 19 | layer_arms | armor |
| 20 | layer_cape | cape |
| 21 | layer_pack | only used by itemid_backpack |
| 22 | layer_robe | robe over all |
| 23 | layer_skirt | skirt or kilt |
| 24 | layer_legs | plate legs |

# Others

these are not part of the paper doll (but get sent to the client)

|  |  |  |
|----|----|----|
| **Layer ID** | **Default Layer Defname** | **Description** |
| 25 | layer_horse | ride this object. (horse objects are strange?) |
| 26 | layer_vendor_stock | the stuff the vendor will restock and sell to the players |
| 27 | layer_vendor_extra | the stuff the vendor will resell to players but is not restocked. (bought from players) |
| 28 | layer_vendor_buys | the stuff the vendor can buy from players but does not stock |
| 29 | layer_bankbox | contents of my bank box |

internally used layers - don't bother sending these to client.

|     |                |                                    |
|-----|----------------|------------------------------------|
| 30  | layer_special  | can be multiple of these. memories |
| 31  | layer_dragging |                                    |

# Spells

|  |  |  |
|----|----|----|
| 32 | layer_spell_stats | stats effecting spell. these cancel each other out |
| 33 | layer_spell_reactive |  |
| 34 | layer_spell_night_sight |  |
| 35 | layer_spell_protection |  |
| 36 | layer_spell_incognito |  |
| 37 | layer_spell_magic_reflect |  |
| 38 | layer_spell_paralyze | or turned to stone |
| 39 | layer_spell_invis |  |
| 40 | layer_spell_polymorph |  |
| 41 | layer_spell_summon | magical summoned creature |

# Flags

|  |  |  |
|----|----|----|
| 42 | layer_flag_poison |  |
| 43 | layer_flag_criminal | criminal or murderer ? |
| 44 | layer_flag_potion | some magic type effect done by a potion. (they cannot be dispelled) |
| 45 | layer_flag_spiritspeak |  |
| 46 | layer_flag_wool | regrowing wool |
| 47 | layer_flag_drunk | booze effect |
| 48 | layer_flag_clientlinger |  |
| 49 | layer_flag_hallucination | shrooms etc |
| 50 | layer_flag_potionused | track the time till we can use a potion again |
| 51 | layer_flag_stuck | in a trap or web |
| 52 | layer_flag_murders | how many murders do we have ? and decay timer |
| 53 | layer_flag_bandage | bandages go here for healing |

[Category:Reference Compendium](Category:Reference_Compendium "wikilink") [Category: Properties and Functions](Category:_Properties_and_Functions "wikilink")
