Have you ever wondered why your handmade set of platemail where each
part has an AR value of "40" only gives you an overall armor rating of
"36"? Well, here is the answer.

Sphere follows OSI's armor rating system. That means, that each armor
part will show you an AR value what it will give you if you wear a
complete set of armor where each part has this AR value. Depending on
what body parts a selected armor part is covering it adds a procentual
share to the overall armor.

Furthermore, armor pieces theoretically can be stacked. So a platemail
chest covers chest and back, and a cloak covers the chest. But that does
not mean that your back now is double protected: Like on OSI, Sphere
only uses the covering part with the highest AR property. Therefore, if
you wear a chain tunic under your plate, id adds to weight, but not to
your character's AR.

### Body parts and Percents

`15 percent from    ARMOR_HEAD`  
`7 percent from    ARMOR_NECK`  
`5 percent from    ARMOR_BACK`  
`25 percent from    ARMOR_CHEST`  
`14 percent from    ARMOR_ARMS`  
`7 percent from    ARMOR_HANDS`  
`22 percent from    ARMOR_LEGS`  
`5 percent from    ARMOR_FEET`  

### What layer covers what?

`LAYER_HELM                                                         gives ARMOR_HEAD`  
`LAYER_COLLAR                                                       gives ARMOR_NECK`  
`LAYER_SHIRT, LAYER_CHEST, LAYER_TUNIC, LAYER_CAPE, LAYER_ROBE      gives ARMOR_BACK`  
`LAYER_SHIRT, LAYER_CHEST, LAYER_TUNIC, LAYER_ROBE                  gives ARMOR_CHEST`  
`LAYER_ARMS, LAYER_CAPE, LAYER_ROBE                                 gives ARMOR_ARMS`  
`LAYER_GLOVES                                                       gives ARMOR_HANDS`  
`LAYER_PANTS, LAYER_SKIRT, LAYER_HALF_APRON, LAYER_ROBE, LAYER_LEGS gives ARMOR_LEGS`  
`LAYER_SHOES, LAYER_LEGS                                            gives ARMOR_FEET`  

### Or, if you're preferring it the other way around:

`A helmet, hat ect. will only cover the head, thus adding 10 percent to the total AR.`  
`A gorget, but also a necklace will cover the neck, adding 5 percent to total AR.`  
`A shirt (LAYER_SHIRT) can cover the back and the chest, adding up to 40 percent of total AR.`  
`Items on LAYER_CHEST and LAYER_TUNIC behave like LAYER_SHIRT.`  
`A cape may cover the back and the arms, adding up to 20 percent to total AR.`  
`A robe may cover back, chest, arms and legs, adding up to 70 percent to total AR.`  
`Armwear (LAYER_ARMS) only covers the arms, thus adding 10 percent to total AR.`  
`Gloves and gauntlets are covering the hands, adding 10 percent.`  
`LAYER_PANTS, LAYER_SKIRT, LAYER_HALF_APRON are covering the legs (20 percent of total AR).`  
`LAYER_LEGS (like plate legs) and LAYER_SHOES are covering the feet (5 percent of total AR)`  

Do not forget that multiple coverings will \_not\_ stack; only the item
with the highest AR property will be taken into account!

If you prefer it all in a combined table:

|            |               |
|------------|---------------|
|            | **Hit Zones** |
|            | head          |
| **layer**  | 10%           |
| helm       | X             |
| collar     | \-            |
| shirt      | \-            |
| chest      | \-            |
| tunic      | \-            |
| cape       | \-            |
| robe       | \-            |
| arms       | \-            |
| gloves     | \-            |
| pants      | \-            |
| skirt      | \-            |
| half apron | \-            |
| legs       | \-            |
| shoes      | \-            |

[Category: Articles](Category:_Articles "wikilink")
