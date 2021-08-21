import bpy
import bmesh

def run():
    #Get the selected object
    ob = bpy.context.object

    #Get object's Shapekeys
    shape_keys = ob.data.shape_keys.key_blocks

    # Duplicate key function
    sk = ob.data.shape_keys.key_blocks

    #ShapeKeys
    cat_names = ["~~EyeBrows~~","~~Mouth~~","~~Eyes~~","~~Other~~","~~NoCat~~","~~FullFace~~"]
    
    for idx,cat in enumerate(cat_names):
        if not cat in ob.data.shape_keys.key_blocks: 
            ob.shape_key_add(name=cat_names[idx])
            print("Generated: "+cat)

    sk_names = ("vrc.blink_left", "vrc.blink_right", "vrc.lowerlid_left", "vrc.lowerlid_right",
                "vrc.v_aa", "vrc.v_ch", "vrc.v_dd", "vrc.v_e", "vrc.v_ff", "vrc.v_ih", "vrc.v_kk", "vrc.v_nn", "vrc.v_oh", "vrc.v_ou", "vrc.v_pp", "vrc.v_rr", "vrc.v_sil", "vrc.v_ss", "vrc.v_th",
                "~~EyeBrows~~",
                    "Anger",
                    "Sadness",
                    "Cheerful",
                    "Serious",
                    "Eyebrow Head Right",
                    "Eyebrow Head Left",
                    "Front",
                    "Upper",
                    "Lower",
                "~~Eyes~~",
                    "Blink",
                    "Wink",
                    "Wink 2",
                    "Wink Right",
                    "Wink 2 Right",
                    "Calm",
                    "Surprised",
                    "Stare",
                    "Slant",
                    "Pupil",
                    "Pupil Vertical Collapse",
                    "HorrorChild !",
                    "Horrorchild!",
                    "Hachu Eye",
                    "Hachu Eye Vertical Collapse",
                    "Hachu Eye Side Collapse",
                    "Blink Happy",
                    "Close><",
                    "Close ><",
                    "Heart",
                    "Star Eye",
                    "Tears",
                    "Light Lower",
                "~~Mouth~~",
                    "Ah",
                    "Ah 2",
                    "Ch",
                    "U",
                    "E",
                    "Oh",
                    "Hmm",
                    "Wa",
                    "Grin",
                    "Grin 2",
                    "Mouth Horn Raise",
                    "Mouth Horn Lower",
                    "Smile",
                    "ω□",
                    "ω",
                    "Lick",
                    "Mouth Side Widen",
                    "TehHeh Lick",
                    "TehHeh Lick 2",
                    "▲",
                    "∧",
                    "□",
                    "Teeth None Upper",
                    "Teeth None Lower",
                    "Sadface",
                    "lewd face",
                "~~Other~~",
                    "Contour",
                    "Blush",
                "~~FullFace~~",
                    "TriFace",
                    ":3",
                    ":3Wide",
                    "Box",
                    "huge ass smile",
                "~~NoCat~~"
                )

    for name in reversed(sk_names):
        idx = sk.find(name)
        if idx != -1:
            ob.active_shape_key_index = idx
            bpy.ops.object.shape_key_move(type='TOP')
    print("Finished")

if __name__ == "__main__":
    run()
