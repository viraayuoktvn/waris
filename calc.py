def hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance):
    if suami > 0:
        if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
            share_suami = (1 / 2) * total_inheritance
        if anak_laki > 0 or cucu_laki > 0 or anak_perempuan > 0 or cucu_perempuan > 0:
            share_suami = (1 / 4) * total_inheritance
        if anak_laki == 0 and cucu_laki == 0:
            if ayah == 0 and kakek == 0 and (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                share_suami = (3 / 13) * total_inheritance
            if ayah == 0 and kakek == 0 and (ibu > 0 or nenek > 0) and anak_perempuan == 1 and cucu_perempuan > 0:
                share_suami = (3 / 13) * total_inheritance

            if (ayah > 0 or kakek > 0 or ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                share_suami = (3 / 13) * total_inheritance
            if (ayah > 0 or kakek > 0 or ibu > 0 or nenek > 0) and anak_perempuan == 1 and cucu_perempuan > 0:
                share_suami = (3 / 13) * total_inheritance

            if (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                share_suami = (3 / 13) * total_inheritance
            if (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                share_suami = (3 / 15) * total_inheritance
            if (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan == 1 and cucu_perempuan > 0:
                share_suami = (3 / 15) * total_inheritance

            if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and anak_perempuan == 0 and cucu_perempuan == 0:
                if saudara_perempuan_kandung >= 2 and saudara_seibu == 0 and ibu == 0 and nenek == 0:
                    share_suami = (3 / 7) * total_inheritance
                if saudara_perempuan_kandung == 1 and saudara_seibu == 1 and ibu == 0 and nenek == 0:
                    share_suami = (3 / 7) * total_inheritance
                if saudara_perempuan_kandung >= 2 and saudara_seibu == 1 and ibu == 0 and nenek == 0:
                    share_suami = (3 / 8) * total_inheritance
                if saudara_perempuan_kandung == 1 and saudara_seibu >= 2 and ibu == 0 and nenek == 0:
                    share_suami = (3 / 8) * total_inheritance
                if saudara_perempuan_kandung >= 2 and saudara_seibu >= 2 and ibu == 0 and nenek == 0:
                    share_suami = (3 / 9) * total_inheritance

                if saudara_perempuan_kandung > 0 and saudara_seibu == 0 and ibu > 0 and nenek == 0:
                    share_suami = (3 / 8) * total_inheritance
                if saudara_perempuan_kandung == 1 and saudara_seibu == 0 and ibu == 0 and nenek > 0:
                    share_suami = (3 / 7) * total_inheritance
                if saudara_perempuan_kandung >= 2 and saudara_seibu == 0 and ibu == 0 and nenek > 0:
                    share_suami = (3 / 8) * total_inheritance

                if saudara_perempuan_kandung == 1 and saudara_seibu == 1 and (ibu > 0 or nenek > 0):
                    share_suami = (3 / 8) * total_inheritance
                if saudara_perempuan_kandung >= 2 and saudara_seibu == 1 and (ibu > 0 or nenek > 0):
                    share_suami = (3 / 9) * total_inheritance
                if saudara_perempuan_kandung == 1 and saudara_seibu >= 2 and (ibu > 0 or nenek > 0):
                    share_suami = (3 / 9) * total_inheritance
                if saudara_perempuan_kandung >= 2 and saudara_seibu >= 2 and (ibu > 0 or nenek > 0):
                    share_suami = (3 / 10) * total_inheritance

        if anak_laki == 0 and cucu_laki > 0:
            if (ayah > 0 or kakek > 0 or ibu > 0 or nenek > 0) and anak_perempuan == 1 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                share_suami = (1 / 4) * total_inheritance
            if (ayah > 0 or kakek > 0 or ibu > 0 or nenek > 0) and anak_perempuan >= 2 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                share_suami = (3 / 13) * total_inheritance
            if (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan == 1 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                share_suami = (3 / 13) * total_inheritance
            if (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan >= 2 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                share_suami = (3 / 15) * total_inheritance
    else :
        share_suami = 0
    return share_suami

def hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance):
    if istri > 0:
        if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
            share_istri = (1 / 4) * total_inheritance
        if (anak_laki > 0 or cucu_laki > 0 or anak_perempuan > 0 or cucu_perempuan > 0):
            share_istri = (1 / 8) * total_inheritance
        if anak_laki == 0 and cucu_laki == 0:
            if (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                share_istri = (3 / 27) * total_inheritance
            if (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan == 1 and cucu_perempuan > 0:
                share_istri = (3 / 27) * total_inheritance
            if (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0) and anak_perempuan >= 2 and cucu_perempuan > 0:
                share_istri = (3 / 15) * total_inheritance

            if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and anak_perempuan == 0 and cucu_perempuan == 0:
                if saudara_seibu == 1 and saudara_perempuan_kandung == 0 and ibu == 0 and nenek == 0:
                    share_istri = (1 / 4) * total_inheritance
                if saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0:
                    share_istri = (3 / 13) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0:
                    share_istri = (3 / 13) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0:
                    share_istri = (3 / 15) * total_inheritance

                if saudara_seibu == 1 and saudara_perempuan_kandung == 1  and (ibu > 0 or nenek > 0):
                    share_istri = (3 / 13) * total_inheritance
                if saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0):
                    share_istri = (3 / 15) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0):
                    share_istri = (3 / 15) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0):
                    share_istri = (3 / 17) * total_inheritance

                if saudara_seibu == 0 and saudara_perempuan_kandung > 0 and ibu > 0:
                    share_istri = (3 / 13) * total_inheritance
                if saudara_seibu == 0 and saudara_perempuan_kandung == 1 and nenek > 0:
                    share_istri = (1 / 4) * total_inheritance
                if saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and nenek > 0:
                    share_istri = (3 / 13) * total_inheritance

        if anak_laki == 0 and anak_perempuan >= 2 and ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0)):
            share_istri = (3 / 27) * total_inheritance
    else:
        share_istri = 0
    return share_istri 

def hitung_bagian_ayah(ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri):
    if ayah > 0:
        share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
        share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
        share_ibu = hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        share_nenek = hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        
        if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
            if suami == 0 and istri == 0 and ibu == 0 and kakek == 0 and nenek == 0:
                share_ayah = total_inheritance
            if ibu > 0 or suami > 0 or istri > 0 or nenek > 0:
                share_ayah = total_inheritance - (share_suami + share_istri + share_ibu + share_nenek)
        if anak_laki > 0 or cucu_laki > 0:
            share_ayah = (1 / 6) * total_inheritance
        if anak_laki == 0 and cucu_laki == 0:
            if (anak_perempuan == 1 or cucu_perempuan == 1) and suami == 0 and istri == 0 and ibu == 0 and nenek == 0:
                share_ayah = (1 / 4) * total_inheritance
            if (anak_perempuan >= 2 or cucu_perempuan >= 2) and suami == 0 and istri == 0 and ibu == 0 and nenek == 0:
                share_ayah = (1 / 5) * total_inheritance
            if anak_perempuan == 1 and cucu_perempuan > 0 and suami == 0 and istri == 0 and ibu == 0 and nenek == 0:
                share_ayah = (1 / 5) * total_inheritance

            if (anak_perempuan == 1 or cucu_perempuan == 1) and suami == 0 and istri == 0 and (ibu > 0 or nenek > 0):
                share_ayah = (1 / 5) * total_inheritance
            if (anak_perempuan >= 2 or cucu_perempuan >= 2) and suami == 0 and istri == 0 and (ibu > 0 or nenek > 0):
                share_ayah = (1 / 6) * total_inheritance
            if anak_perempuan > 0 and cucu_perempuan > 0 and suami == 0 and istri == 0 and (ibu > 0 or nenek > 0):
                share_ayah = (1 / 6) * total_inheritance

            if suami > 0 and istri == 0:
                if ibu == 0 and nenek == 0 and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_ayah = (3 / 16) * total_inheritance
                if ibu == 0 and nenek == 0 and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_ayah = (2 / 13) * total_inheritance
                if ibu == 0 and nenek == 0 and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_ayah = (2 / 13) * total_inheritance

                if (ibu > 0 or nenek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_ayah = (2 / 13) * total_inheritance
                if (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_ayah = (2 / 15) * total_inheritance
                if (ibu > 0 or nenek > 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_ayah = (2 / 15) * total_inheritance

            if istri > 0 and suami == 0:
                if ibu == 0 and nenek == 0 and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_ayah = (7 / 32) * total_inheritance
                if ibu == 0 and nenek == 0 and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_ayah = (7 / 40) * total_inheritance
                if ibu == 0 and nenek == 0 and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_ayah = (7 / 40) * total_inheritance

                if (ibu > 0 or nenek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_ayah = (7 / 40) * total_inheritance
                if (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_ayah = (4 / 27) * total_inheritance
                if (ibu > 0 or nenek > 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_ayah = (4 / 27) * total_inheritance

        if cucu_laki > 0:
            if cucu_perempuan > 0:
                share_ayah = (1 / 6) * total_inheritance
            if anak_laki == 0 and suami > 0 and istri == 0 and ibu == 0 and nenek == 0 and anak_perempuan >= 2:
                share_ayah = (2 / 13) * total_inheritance
            if anak_laki == 0 and suami > 0 and istri == 0 and (ibu > 0 or nenek > 0) and anak_perempuan > 0:
                share_ayah = (2 / 13) * total_inheritance
            if anak_laki == 0 and suami > 0 and istri == 0 and (ibu > 0 or nenek > 0) and anak_perempuan >= 2:
                share_ayah = (2 / 15) * total_inheritance

            if anak_laki == 0 and cucu_perempuan == 0 and anak_perempuan == 0 and suami == 0 and istri == 0 and ibu == 0 and nenek == 0:
                share_ayah = (ayah / (ayah + cucu_laki)) * total_inheritance
            if anak_laki == 0 and cucu_perempuan == 0 and anak_perempuan == 0 and ((ibu > 0 or suami > 0 or istri > 0 or nenek > 0) or ((suami > 0 or istri > 0) and (ibu > 0 or nenek > 0))):
                share_ayah = (ayah / (ayah + cucu_laki)) * (total_inheritance - (share_suami + share_istri + share_ibu + share_nenek))
            
            if anak_laki == 0 and anak_perempuan == 1 and istri > 0 and suami == 0 and (ibu > 0 or nenek > 0):
                share_ayah = (1 / 6) * total_inheritance
            if anak_laki == 0 and anak_perempuan >= 2 and istri > 0 and suami == 0 and (ibu > 0 or nenek > 0):
                share_ayah = (4 / 27) * total_inheritance
    else:
        share_ayah = 0

    return share_ayah

def hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri):
    if ibu > 0:
        share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
        share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
   
        if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
            if suami == 0 and istri == 0 and ayah == 0 and kakek == 0 and nenek == 0 and saudara_seibu == 0:
                share_ibu = total_inheritance
            if suami == 0 and istri == 0 and (ayah > 0 or kakek > 0):
                share_ibu = (1 / 3) * total_inheritance
            if (suami > 0 or istri > 0) and ayah == 0 and kakek == 0 and saudara_seibu == 0:
                share_ibu = total_inheritance - (share_suami + share_istri)

            if suami > 0 and ayah > 0 and istri == 0 and kakek == 0:
                share_ibu = (1 / 6) * total_inheritance
            if suami > 0 and kakek > 0 and istri == 0 and ayah == 0:
                share_ibu = (1 / 3) * total_inheritance
            if istri > 0 and ayah > 0 and suami == 0 and kakek == 0:
                share_ibu = (1 / 4) * total_inheritance
            if istri > 0 and kakek > 0 and suami == 0 and ayah == 0:
                share_ibu = (1 / 3) * total_inheritance
        if anak_laki > 0 or cucu_laki > 0 or saudara_laki_kandung > 0:
            share_ibu = (1 / 6) * total_inheritance
        if anak_laki == 0 and cucu_laki == 0:
            if suami == 0 and istri == 0:
                if (ayah == 0 and kakek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1) and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_ibu = (1 / 4) * total_inheritance
                if (ayah == 0 and kakek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2) and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_ibu = (1 / 5) * total_inheritance
                if (ayah == 0 and kakek == 0) and anak_perempuan > 0 and cucu_perempuan > 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_ibu = (1 / 5) * total_inheritance

                if (ayah > 0 or kakek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_ibu = (1 / 5) * total_inheritance
                if (ayah > 0 or kakek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_ibu = (1 / 6) * total_inheritance
                if (ayah > 0 or kakek > 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_ibu = (1 / 6) * total_inheritance
            
            if saudara_laki_kandung == 1 and anak_perempuan == 0 and cucu_perempuan == 0 and saudara_perempuan_kandung == 0 and saudara_seibu == 0:
                share_ibu = (1 / 3) * total_inheritance
                    
            if suami > 0:
                if (ayah == 0 and kakek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1) and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_ibu = (3 / 16) * total_inheritance
                if (ayah == 0 and kakek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2) and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_ibu = (2 / 13) * total_inheritance
                if (ayah == 0 and kakek == 0) and anak_perempuan > 0 and cucu_perempuan > 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_ibu = (2 / 13) * total_inheritance

                if (ayah > 0 or kakek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_ibu = (2 / 13) * total_inheritance
                if (ayah > 0 or kakek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_ibu = (2 / 15) * total_inheritance
                if (ayah > 0 or kakek > 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_ibu = (2 / 15) * total_inheritance
                
            if istri > 0:
                if (ayah == 0 and kakek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1) and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_ibu = (7 / 32) * total_inheritance
                if (ayah == 0 and kakek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2) and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_ibu = (7 / 40) * total_inheritance
                if (ayah == 0 and kakek == 0) and anak_perempuan > 0 and cucu_perempuan > 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_ibu = (7 / 40) * total_inheritance

                if (ayah > 0 or kakek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_ibu = (7 / 40) * total_inheritance
                if (ayah > 0 or kakek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_ibu = (4 / 27) * total_inheritance
                if (ayah > 0 or kakek > 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_ibu = (4 / 27) * total_inheritance
                
            if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and anak_perempuan == 0 and cucu_perempuan == 0:
                if saudara_seibu == 0 and saudara_perempuan_kandung == 1 and suami == 0 and istri == 0:
                    share_ibu = (2 / 5) * total_inheritance
                if saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and suami == 0 and istri == 0:
                    share_ibu = (1 / 5) * total_inheritance
                if saudara_seibu == 1 and saudara_perempuan_kandung == 0 and suami == 0 and istri == 0:
                    share_ibu = (2 / 3) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung == 0 and suami == 0 and istri == 0:
                    share_ibu = (1/ 3) * total_inheritance
                if saudara_seibu == 1 and saudara_perempuan_kandung == 1 and suami == 0 and istri == 0:
                    share_ibu = (1 / 5) * total_inheritance
                if saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and suami == 0 and istri == 0:
                    share_ibu = (1 / 6) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and suami == 0 and istri == 0:
                    share_ibu = (1 / 6) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and suami == 0 and istri == 0:
                    share_ibu = (1 / 7) * total_inheritance
                        
                if saudara_seibu == 1 and saudara_perempuan_kandung == 0 and suami > 0 and istri == 0:
                    share_ibu = (1 / 3) * total_inheritance     
                if saudara_seibu >= 2 and saudara_perempuan_kandung == 0 and suami > 0 and istri == 0:
                    share_ibu = (1 / 6) * total_inheritance   
                if saudara_seibu == 0 and saudara_perempuan_kandung == 1 and suami > 0 and istri == 0:
                    share_ibu = (2 / 8) * total_inheritance
                if saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and suami > 0 and istri == 0:
                    share_ibu = (1 / 8) * total_inheritance
                if saudara_seibu == 1 and saudara_perempuan_kandung == 1 and suami > 0 and istri == 0:
                    share_ibu = (1 / 8) * total_inheritance
                if saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and suami > 0 and istri == 0:
                    share_ibu = (1 / 9) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and suami > 0 and istri == 0:
                    share_ibu = (1 / 9) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and suami > 0 and istri == 0:
                    share_ibu = (1 / 10) * total_inheritance

                if saudara_seibu == 1 and saudara_perempuan_kandung == 0 and suami == 0 and istri > 0:
                    share_ibu = (1 / 2) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung == 0 and suami == 0 and istri > 0:
                    share_ibu = (1 / 4) * total_inheritance
                if saudara_seibu == 0 and saudara_perempuan_kandung == 1 and suami == 0 and istri > 0:
                    share_ibu = (4 / 13) * total_inheritance
                if saudara_seibu == 0 and saudara_perempuan_kandung >= 2 and suami == 0 and istri > 0:
                    share_ibu = (2 / 13) * total_inheritance
                if saudara_seibu == 1 and saudara_perempuan_kandung == 1 and suami == 0 and istri > 0:
                    share_ibu = (2 / 13) * total_inheritance
                if saudara_seibu == 1 and saudara_perempuan_kandung >= 2 and suami == 0 and istri > 0:
                    share_ibu = (2 / 15) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung == 1 and suami == 0 and istri > 0:
                    share_ibu = (2 / 15) * total_inheritance
                if saudara_seibu >= 2 and saudara_perempuan_kandung >= 2 and suami == 0 and istri > 0:
                    share_ibu = (2 / 17) * total_inheritance

            if ayah == 0 and kakek == 0 and (anak_perempuan == 1 or cucu_perempuan == 1) and ((saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0) or (saudara_laki_kandung > 0 and saudara_perempuan_kandung > 0)):
                share_ibu = (1 / 6) * total_inheritance
            if ayah == 0 and kakek == 0 and suami == 0 and istri == 0 and (anak_perempuan > 0 or cucu_perempuan > 0) and (saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0):
                share_ibu = (1 / 6) * total_inheritance
            if ayah == 0 and kakek == 0 and suami > 0 and istri == 0 and (anak_perempuan >= 2 or cucu_perempuan >= 2) and ((saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0)):
                share_ibu = (2 / 13) * total_inheritance
            if ayah == 0 and kakek == 0 and istri > 0 and istri == 0 and (anak_perempuan >= 2 or cucu_perempuan >= 2) and ((saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0)):
                share_ibu = (1 / 6) * total_inheritance

        if anak_laki == 0 and cucu_laki > 0:
            if suami > 0 and anak_perempuan >= 2 and ayah == 0 and kakek == 0:
                share_ibu = (2 / 13) * total_inheritance
            if suami > 0 and anak_perempuan == 1 and (ayah > 0 or kakek > 0):
                share_ibu = (2 / 13) * total_inheritance
            if suami > 0 and anak_perempuan >= 2 and (ayah > 0 or kakek > 0):
                share_ibu = (2 / 15) * total_inheritance
            
            if istri > 0 and anak_perempuan >= 2 and (ayah > 0 or kakek > 0):
                share_ibu = (4 / 27) * total_inheritance
    else:       
        share_ibu = 0

    return share_ibu

def hitung_bagian_kakek(kakek, ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri):
    if kakek > 0 and ayah == 0:
        share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
        share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
        share_ibu = hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        share_nenek = hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
    
        if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
            if suami == 0 and istri == 0 and ayah == 0 and ibu == 0 and nenek == 0:
                share_kakek = total_inheritance
            if (ibu > 0 or suami > 0 or istri > 0 or nenek > 0):
                share_kakek = total_inheritance - (share_suami + share_istri + share_ibu + share_nenek)
        if anak_laki > 0 or cucu_laki > 0:  
            share_kakek = (1 / 6) * total_inheritance
        if anak_laki == 0 and cucu_laki == 0:
            if (ibu == 0 and nenek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                share_kakek = (1 / 4) * total_inheritance
            if (ibu == 0 and nenek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                share_kakek = (1 / 5) * total_inheritance
            if (ibu == 0 and nenek == 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                share_kakek = (1 / 5) * total_inheritance

            if (ibu > 0 or nenek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                share_kakek = (1 / 5) * total_inheritance
            if (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                share_kakek = (1 / 6) * total_inheritance
            if (ibu > 0 or nenek > 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                share_kakek = (1 / 6) * total_inheritance

            if suami > 0:
                if (ibu == 0 and nenek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_kakek = (3 / 16) * total_inheritance
                if (ibu == 0 and nenek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_kakek = (2 / 13) * total_inheritance
                if (ibu == 0 and nenek == 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_kakek = (2 / 13) * total_inheritance

                if (ibu > 0 or nenek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_kakek = (2 / 13) * total_inheritance
                if (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_kakek = (2 / 15) * total_inheritance
                if (ibu > 0 or nenek > 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_kakek = (2 / 15) * total_inheritance
                        
            if istri > 0:
                if (ibu == 0 and nenek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_kakek = (7 / 32) * total_inheritance
                if (ibu == 0 and nenek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_kakek = (7 / 40) * total_inheritance
                if (ibu == 0 and nenek == 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_kakek = (7 / 40) * total_inheritance

                if (ibu > 0 or nenek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_kakek = (7 / 40) * total_inheritance
                if (ibu > 0 or nenek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_kakek = (4 / 27) * total_inheritance
                if (ibu > 0 or nenek > 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_kakek = (4 / 27) * total_inheritance

        if anak_laki == 0 and cucu_laki > 0:
            if suami > 0 and anak_perempuan == 1 and ibu == 0 and nenek == 0:
                share_kakek = (1 / 6) * total_inheritance
            if suami > 0 and anak_perempuan >= 2 and ibu == 0 and nenek == 0:
                share_kakek = (1 / 6) * total_inheritance
            if suami > 0 and anak_perempuan > 0 and ibu == 0 and nenek == 0:
                share_kakek = (2 / 13) * total_inheritance
            if suami > 0 and anak_perempuan == 1 and (ibu > 0 or nenek > 0):
                share_kakek = (2 / 13) * total_inheritance
            if suami > 0 and anak_perempuan >= 2 and (ibu > 0 or nenek > 0):
                share_kakek = (2 / 15) * total_inheritance

            if istri > 0 and anak_perempuan > 0 and ibu == 0 and nenek == 0:
                share_kakek = (1 / 6) * total_inheritance
            if istri > 0 and anak_perempuan == 1 and (ibu > 0 or nenek > 0):
                share_kakek = (1 / 6) * total_inheritance
            if istri > 0 and anak_perempuan >= 2 and (ibu > 0 or nenek > 0):
                share_kakek = (4 / 27) * total_inheritance
    else:
        share_kakek = 0
    return share_kakek

def hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri):
    if nenek > 0 and ibu == 0:        
        share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
        share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)

        if anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
            if suami == 0 and istri == 0 and ayah == 0 and ibu == 0 and kakek == 0 and saudara_seibu == 0:
                share_nenek = total_inheritance
            if (ayah > 0 or suami > 0 or istri > 0 or kakek > 0) and saudara_seibu == 0:
                share_nenek = total_inheritance - (share_suami + share_istri)
            if (ayah > 0 or kakek > 0) and ((suami > 0 or istri > 0) or (suami == 0 and istri == 0)):
                share_nenek = (1 / 6) * total_inheritance
        if anak_laki > 0 or cucu_laki > 0 or anak_perempuan > 0 or cucu_perempuan > 0 or saudara_laki_kandung > 0:  
            share_nenek = (1 / 6) * total_inheritance
        if anak_laki == 0 and cucu_laki == 0:
            if ayah == 0 and kakek == 0 and (anak_perempuan == 1 or cucu_perempuan == 1) and suami == 0 and istri == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                share_nenek = (1 / 4) * total_inheritance
            if ayah == 0 and kakek == 0 and (anak_perempuan >= 2 or cucu_perempuan >= 2) and suami == 0 and istri == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                share_nenek = (1 / 5) * total_inheritance
            if (ayah == 0 and kakek == 0) and anak_perempuan > 0 and cucu_perempuan > 0 and suami == 0 and istri == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                share_nenek = (1 / 5) * total_inheritance

            if (ayah > 0 or kakek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1) and suami == 0 and istri == 0:
                share_nenek = (1 / 5) * total_inheritance
            if (ayah > 0 or kakek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2) and suami == 0 and istri == 0:
                share_nenek = (1 / 6) * total_inheritance
            if (ayah > 0 or kakek > 0) and anak_perempuan > 0 and cucu_perempuan > 0 and suami == 0 and istri == 0:
                share_nenek = (1 / 6) * total_inheritance

            if suami > 0 and istri == 0:
                if (ayah == 0 and kakek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1) and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_nenek = (3 / 16) * total_inheritance
                if (ayah == 0 and kakek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_nenek = (2 / 13) * total_inheritance
                if (ayah == 0 and kakek == 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_nenek = (2 / 13) * total_inheritance

                if (ayah > 0 or kakek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_nenek = (2 / 13) * total_inheritance
                if (ayah > 0 or kakek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_nenek = (2 / 15) * total_inheritance
                if (ayah > 0 or kakek > 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_nenek = (2 / 15) * total_inheritance

            if istri > 0 and suami == 0:
                if (ayah == 0 and kakek == 0) and (anak_perempuan == 1 or cucu_perempuan == 1) and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_nenek = (7 / 32) * total_inheritance
                if (ayah == 0 and kakek == 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2) and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_nenek = (7 / 40) * total_inheritance
                if (ayah == 0 and kakek == 0) and anak_perempuan > 0 and cucu_perempuan > 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    share_nenek = (7 / 40) * total_inheritance

                if (ayah > 0 or kakek > 0) and (anak_perempuan == 1 or cucu_perempuan == 1):
                    share_nenek = (7 / 40) * total_inheritance
                if (ayah > 0 or kakek > 0) and (anak_perempuan >= 2 or cucu_perempuan >= 2):
                    share_nenek = (4 / 27) * total_inheritance
                if (ayah > 0 or kakek > 0) and anak_perempuan > 0 and cucu_perempuan > 0:
                    share_nenek = (4 / 27) * total_inheritance
                    
            if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and anak_perempuan == 0 and cucu_perempuan == 0:
                if suami == 0 and istri == 0:
                    if saudara_seibu == 1 and saudara_perempuan_kandung == 0:
                        share_nenek = (1 / 2) * total_inheritance
                    if saudara_seibu >= 2 and saudara_perempuan_kandung == 0:
                        share_nenek = (1 / 3) * total_inheritance
                    if saudara_seibu == 0 and saudara_perempuan_kandung == 1:
                        share_nenek = (1 / 4) * total_inheritance
                    if saudara_seibu == 0 and saudara_perempuan_kandung >= 2:
                        share_nenek = (1 / 5) * total_inheritance
                    if saudara_seibu == 1 and saudara_perempuan_kandung == 1:
                        share_nenek = (1 / 5) * total_inheritance
                    if saudara_seibu == 1 and saudara_perempuan_kandung >= 2:
                        share_nenek = (1 / 6) * total_inheritance
                    if saudara_seibu >= 2 and saudara_perempuan_kandung == 1:
                        share_nenek = (1 / 6) * total_inheritance
                    if saudara_seibu >= 2 and saudara_perempuan_kandung >= 2:
                        share_nenek = (1 / 7) * total_inheritance

                if suami > 0:
                    if saudara_seibu == 1 and saudara_perempuan_kandung == 0:
                        share_nenek = (1 / 4) * total_inheritance
                    if saudara_seibu >= 2 and saudara_perempuan_kandung == 0:
                        share_nenek = (1 / 6) * total_inheritance
                    if saudara_seibu == 0 and saudara_perempuan_kandung == 1:
                        share_nenek = (1 / 7) * total_inheritance
                    if saudara_seibu == 0 and saudara_perempuan_kandung >= 2:
                        share_nenek = (1 / 8) * total_inheritance
                    if saudara_seibu == 1 and saudara_perempuan_kandung == 1:
                        share_nenek = (1 / 8) * total_inheritance
                    if saudara_seibu == 1 and saudara_perempuan_kandung >= 2:
                        share_nenek = (1 / 9) * total_inheritance
                    if saudara_seibu >= 2 and saudara_perempuan_kandung == 1:
                        share_nenek = (1 / 9) * total_inheritance
                    if saudara_seibu >= 2 and saudara_perempuan_kandung >= 2:
                        share_nenek = (1 / 10) * total_inheritance

                if istri > 0:
                    if saudara_seibu == 1 and saudara_perempuan_kandung == 0:
                        share_nenek = (3 / 8) * total_inheritance
                    if saudara_seibu >= 2 and saudara_perempuan_kandung == 0:
                        share_nenek = (1 / 4) * total_inheritance    
                    if saudara_seibu == 0 and saudara_perempuan_kandung == 1:
                        share_nenek = (3 / 16) * total_inheritance
                    if saudara_seibu == 0 and saudara_perempuan_kandung >= 2:
                        share_nenek = (2 / 13) * total_inheritance
                    if saudara_seibu == 1 and saudara_perempuan_kandung == 1:
                        share_nenek = (2 / 13) * total_inheritance
                    if saudara_seibu == 1 and saudara_perempuan_kandung >= 2:
                        share_nenek = (2 / 15) * total_inheritance
                    if saudara_seibu >= 2 and saudara_perempuan_kandung == 1:
                        share_nenek = (2 / 15) * total_inheritance
                    if saudara_seibu >= 2 and saudara_perempuan_kandung >= 2:
                        share_nenek = (2 / 17) * total_inheritance

        if anak_laki == 0 and cucu_laki > 0:
            if suami > 0 and anak_perempuan >= 2 and ayah == 0 and kakek == 0:
                share_nenek = (2 / 13) * total_inheritance
            if suami > 0 and anak_perempuan == 1 and ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0)):
                share_nenek = (2 / 13) * total_inheritance
            if suami > 0 and anak_perempuan >= 2 and ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0)):
                share_nenek = (2 / 15) * total_inheritance
            if istri > 0 and anak_perempuan >= 2 and ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0)):
                share_nenek = (4 / 27) * total_inheritance
        if anak_laki > 0 and anak_perempuan > 0 and (ayah > 0 or kakek > 0):
            share_nenek = (2 / 13) * total_inheritance
    else:
        share_nenek = 0

    return share_nenek    

def hitung_bagian_anak_laki(anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek):
    if anak_laki > 0:
        share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
        share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
        share_ayah = hitung_bagian_ayah(ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
        share_ibu = hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        share_kakek = hitung_bagian_kakek(kakek, ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
        share_nenek = hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)

        if anak_perempuan == 0:
            if suami == 0 and istri == 0 and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0:
                share_al = total_inheritance
            if anak_perempuan == 0 and (suami > 0 or istri > 0 or ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0):
                share_al = total_inheritance - (share_suami + share_istri + share_ayah + share_ibu + share_kakek + share_nenek)
        if anak_perempuan > 0:
            share_al = ((2 * anak_laki)/(anak_perempuan + (2 * anak_laki))) * (total_inheritance - (share_suami + share_istri + share_ayah + share_ibu + share_kakek + share_nenek))
    else:
        share_al = 0
    return share_al

def hitung_bagian_anak_perempuan(anak_perempuan, anak_laki, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung):
    if anak_perempuan > 0:
        share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
        share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
        share_ayah = hitung_bagian_ayah(ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
        share_ibu = hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        share_kakek = hitung_bagian_kakek(kakek, ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
        share_nenek = hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)

        if anak_laki == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
            if cucu_laki == 0 and cucu_perempuan == 0 and suami == 0 and istri == 0 and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0:
                share_ap = total_inheritance
            if (suami > 0 or istri > 0 or ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0):
                share_ap = total_inheritance - (share_suami + share_istri + share_ayah + share_ibu + share_kakek + share_nenek)
        if anak_laki > 0:
            share_ap = ((anak_perempuan/(anak_perempuan + (2 * anak_laki)))) * (total_inheritance - (share_suami + share_istri + share_ayah + share_ibu + share_kakek + share_nenek))
        if anak_laki == 0:
            if anak_perempuan == 1:
                if ayah == 0 and kakek == 0 and suami == 0 and istri == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    if (ibu > 0 or nenek > 0 or cucu_perempuan > 0):
                        share_ap = (3 / 4) * total_inheritance 
                if (ayah > 0 or kakek > 0) and suami == 0 and istri == 0:
                    if ibu == 0 and nenek == 0:
                        share_ap = (3 / 4) * total_inheritance
                    if (ibu > 0 or nenek > 0):
                        share_ap = (3 / 5) * total_inheritance
                if saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0:
                    share_ap = (1 / 2) * total_inheritance

                if suami > 0:
                    if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                        if ibu == 0 and nenek == 0 and cucu_perempuan == 0:
                            share_ap = (3 / 4) * total_inheritance
                        if (ibu > 0 or nenek > 0 or cucu_perempuan > 0):
                             share_ap = (9 / 16) * total_inheritance
                        if (ibu > 0 or nenek > 0) and cucu_perempuan == 0:
                            share_ap = (9 / 16) * total_inheritance
                        if (ibu > 0 or nenek > 0) and cucu_perempuan > 0:
                            share_ap = (6 / 13) * total_inheritance
                    if ayah > 0 or kakek > 0:
                        if ibu == 0 and nenek == 0 and cucu_perempuan == 0:
                            share_ap = (9 / 16) * total_inheritance
                        if ibu == 0 and nenek == 0 and cucu_perempuan > 0:
                            share_ap = (6 / 13) * total_inheritance
                        if (ibu > 0 or nenek > 0) and cucu_perempuan == 0:
                            share_ap = (6 / 13) * total_inheritance
                        if (ibu > 0 or nenek > 0) and cucu_perempuan > 0:
                            share_ap = (6 / 15) * total_inheritance

                if istri > 0:
                    if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                        if ibu == 0 and nenek == 0 and cucu_perempuan == 0:
                            share_ap = (7 / 8) * total_inheritance
                        if (ibu > 0 or nenek > 0 or cucu_perempuan > 0):
                            share_ap = (21 / 32) * total_inheritance
                        if (ibu > 0 or nenek > 0) and cucu_perempuan == 0:
                            share_ap = (21 / 32) * total_inheritance
                        if (ibu > 0 or nenek > 0) and cucu_perempuan > 0:
                            share_ap = (21 / 40) * total_inheritance
                    if ayah > 0 or kakek > 0:
                        if ibu == 0 and nenek == 0 and cucu_perempuan == 0:
                            share_ap = (21 / 32) * total_inheritance
                        if ibu == 0 and nenek == 0 and cucu_perempuan > 0:
                            share_ap = (21 / 40) * total_inheritance
                        if (ibu > 0 or nenek > 0) and cucu_perempuan == 0:
                            share_ap = (21 / 40) * total_inheritance
                        if (ibu > 0 or nenek > 0) and cucu_perempuan > 0:
                            share_ap = (12 / 27) * total_inheritance

                if cucu_laki > 0:
                    if suami > 0 and ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0)):
                        share_ap = (6 / 13) * total_inheritance
                    else:
                        share_ap = (1 / 2) * total_inheritance
                        
                if cucu_laki == 0 and cucu_perempuan > 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    if suami == 0 and istri == 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0):
                        share_ap = (3 / 5) * total_inheritance
                    if suami == 0 and istri == 0 and ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0)):
                        share_ap = (1 / 2) * total_inheritance

                    if suami > 0 and ibu == 0 and ayah == 0 and kakek == 0 and nenek == 0:
                        share_ap = (9 / 16) * total_inheritance
                    if suami > 0 and (ibu > 0 or ayah > 0 or kakek > 0 or nenek > 0):
                        share_ap = (6 / 13) * total_inheritance
                    if suami > 0 and ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0)):
                        share_ap = (6 / 15) * total_inheritance

                    if istri > 0 and ibu == 0 and ayah == 0 and kakek == 0 and nenek == 0:
                        share_ap = (21 / 32) * total_inheritance
                    if istri > 0 and (ibu > 0 or ayah > 0 or kakek > 0 or nenek > 0):
                        share_ap = (21 / 40) * total_inheritance
                    if istri > 0 and ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0)):
                        share_ap = (12 / 27) * total_inheritance

            if anak_perempuan >= 2:
                if cucu_laki == 0 and cucu_perempuan > 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0 and suami == 0 and istri == 0 and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0:
                    share_ap = total_inheritance
                
                if ayah == 0 and kakek == 0 and suami == 0 and istri == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    if ibu > 0 or nenek > 0:
                        share_ap = (4 / 5) * total_inheritance
                if (ayah > 0 or kakek > 0) and suami == 0 and istri == 0:
                    if ibu == 0 and nenek == 0:
                        share_ap = (4 / 5) * total_inheritance
                    if ibu > 0 or nenek > 0:
                        share_ap = (2 / 3) * total_inheritance
                if saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0:
                    share_ap = (2 / 3) * total_inheritance

                if suami > 0:
                    if ayah == 0 and kakek == 0:
                        if ibu == 0 and nenek == 0 and cucu_perempuan == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                            share_ap = (3 / 4) * total_inheritance
                        if ibu > 0 or nenek > 0:
                            share_ap = (8 / 13) * total_inheritance
                    if ayah > 0 or kakek > 0:
                        if ibu == 0 and nenek == 0:
                            share_ap = (8 / 13) * total_inheritance
                        if ibu > 0 or nenek > 0:
                            share_ap = (8 / 15) * total_inheritance

                if istri > 0:
                    if ayah == 0 and kakek == 0:
                        if ibu == 0 and nenek == 0 and cucu_perempuan == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                            share_ap = (7 / 8) * total_inheritance
                        if ibu > 0 or nenek > 0:
                            share_ap = (7 / 10) * total_inheritance
                    if ayah > 0 or kakek > 0:
                        if ibu == 0 and nenek == 0:
                            share_ap = (7 / 10) * total_inheritance
                        if ibu > 0 or nenek > 0:
                            share_ap = (16 / 27) * total_inheritance

                if cucu_laki > 0:
                    share_ap = (2 / 3) * total_inheritance

                    if suami > 0 and (ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0):
                        share_ap = (8 / 13) * total_inheritance
                    if suami > 0 and (ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0):
                        share_ap = (8 / 15) * total_inheritance
                    if istri > 0 and ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0)):
                        share_ap = (16 / 27) * total_inheritance
    else:
        share_ap = 0

    return share_ap

def hitung_bagian_cucu_laki(cucu_laki, anak_laki, cucu_perempuan, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek):
    if cucu_laki > 0 and anak_laki == 0:
        share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
        share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
        share_ap = hitung_bagian_anak_perempuan(anak_perempuan, anak_laki, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung)
        share_ayah = hitung_bagian_ayah(ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
        share_ibu = hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        share_kakek = hitung_bagian_kakek(kakek, ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
        share_nenek = hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)

        sisa1 = total_inheritance - (share_suami + share_istri + share_ap + share_ayah + share_ibu + share_kakek + share_nenek)
        sisa2 = total_inheritance - (share_suami + share_istri + share_ap + share_ibu + share_kakek + share_nenek)
        
        if cucu_perempuan == 0 and anak_perempuan == 0 and suami == 0 and istri == 0 and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0:
            share_cl = total_inheritance
        if cucu_perempuan == 0:
            if (suami > 0 or istri > 0 or ibu > 0 or kakek > 0 or nenek > 0 or anak_perempuan > 0) and ayah == 0:
                share_cl = sisa1
            if ayah > 0 and suami == 0 and istri == 0 and ibu == 0 and kakek == 0 and nenek == 0 and anak_perempuan == 0:
                share_cl = (cucu_laki/(ayah + cucu_laki)) * total_inheritance
            if ayah > 0 and (suami > 0 or istri > 0 or ibu > 0 or kakek > 0 or nenek > 0) and anak_perempuan == 0:
                share_cl = (cucu_laki/(ayah + cucu_laki)) * sisa2
            if ayah > 0 and anak_perempuan > 0:
                share_cl = sisa1
            if anak_perempuan >= 2:
                share_cl = ((2 * cucu_laki )/(cucu_perempuan + (2 * cucu_laki))) * sisa1
        if cucu_perempuan > 0:
            if suami > 0 and anak_perempuan >= 2 and ((ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0) or ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0))):
                share_cl = 0
            if anak_perempuan == 0 and (suami > 0 or istri > 0) and ((ayah > 0 and (ibu > 0 or nenek > 0))):
                share_cl = (cucu_laki/(ayah + cucu_laki)) * sisa2
            if anak_perempuan >= 2 and suami > 0 and ((ayah > 0 and ibu > 0) or (ayah > 0 and nenek > 0)):
                share_cl = 0
            else:
                share_cl = ((2 * cucu_laki )/(cucu_perempuan + (2 * cucu_laki))) * sisa1
    else:
        share_cl = 0
    return share_cl

def hitung_bagian_cucu_perempuan(cucu_perempuan, cucu_laki, anak_laki, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek):
    if cucu_perempuan > 0 and anak_laki == 0:
        share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
        share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
        share_ap = hitung_bagian_anak_perempuan(anak_perempuan, anak_laki, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung)
        share_ayah = hitung_bagian_ayah(ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
        share_ibu = hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        share_kakek = hitung_bagian_kakek(kakek, ayah, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_ibu, share_nenek, share_suami, share_istri)
        share_nenek = hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)

        if cucu_laki == 0 and saudara_seibu == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
            if anak_perempuan == 0 and suami == 0 and istri == 0 and ayah == 0 and ibu == 0 and kakek == 0 and nenek == 0:
                share_cp = total_inheritance
            if (anak_perempuan > 0 or suami > 0 or istri > 0 or ayah > 0 or ibu > 0 or kakek > 0 or nenek > 0):
                share_cp = total_inheritance - (share_suami + share_istri + share_ap + share_ayah + share_ibu + share_kakek + share_nenek)
        
        if cucu_laki > 0:
            if anak_perempuan > 0 and suami > 0 and ((ayah > 0 or kakek > 0) and (ibu > 0 or nenek > 0)):
                share_cp = 0
            else:
                share_cp = ((cucu_perempuan)/(cucu_perempuan + (2 * cucu_laki))) * (total_inheritance - (share_suami + share_istri + share_ap + share_ayah + share_ibu + share_kakek + share_nenek))

        if cucu_laki == 0:
            if anak_perempuan == 0 and cucu_perempuan == 1:
                # share_cp = (1 / 2) * total_inheritance
                if (saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0):
                    share_cp = (1 / 2) * total_inheritance
                if ayah == 0 and kakek == 0 and suami == 0 and istri == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    if ibu > 0 or nenek > 0:
                        share_cp = (3 / 4) * total_inheritance
                if (ayah > 0 or kakek > 0) and suami == 0 and istri == 0:
                    if ibu == 0 and nenek == 0:
                        share_cp = (3 / 4) * total_inheritance
                    if ibu > 0 or nenek > 0:
                        share_cp = (3 / 5) * total_inheritance

                if suami > 0:
                    if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                        if ibu > 0 or nenek > 0:
                            share_cp = (9 / 16) * total_inheritance
                    if ayah > 0 or kakek > 0:
                        if ibu == 0 and nenek == 0:
                            share_cp = (9 / 16) * total_inheritance
                        if ibu > 0 or nenek > 0:
                            share_cp = (6 / 13) * total_inheritance

                if istri > 0:
                    if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                        if ibu > 0 or nenek > 0:
                            share_cp = (21 / 32) * total_inheritance
                    if ayah > 0 or kakek > 0:
                        if ibu == 0 and nenek == 0:
                            share_cp = (21 / 32) * total_inheritance
                        if ibu > 0 or nenek > 0:
                            share_cp = (21 / 40) * total_inheritance

            if anak_perempuan == 0 and cucu_perempuan >= 2:
                # share_cp = (2 / 3) * total_inheritance
                if (saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0):
                    share_cp = (2 / 3) * total_inheritance
                if ayah == 0 and kakek == 0 and suami == 0 and istri == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    if ibu > 0 or nenek > 0:
                        share_cp = (4 / 5) * total_inheritance
                if (ayah > 0 or kakek > 0) and suami == 0 and istri == 0:
                    if ibu == 0 and nenek == 0:
                        share_cp = (4 / 5) * total_inheritance
                    if ibu > 0 or nenek > 0:
                        share_cp = (2 / 3) * total_inheritance

                if suami > 0:
                    if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                        if ibu > 0 or nenek > 0:
                            share_cp = (8 / 13) * total_inheritance
                    if ayah > 0 or kakek > 0:
                        if ibu == 0 and nenek == 0:
                            share_cp = (8 / 13) * total_inheritance
                        if ibu > 0 or nenek > 0:
                            share_cp = (8 / 15) * total_inheritance

                if istri > 0:
                    if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                        if ibu > 0 or nenek > 0:
                            share_cp = (7 / 10) * total_inheritance
                    if ayah > 0 or kakek > 0:
                        if ibu == 0 and nenek == 0:
                            share_cp = (7 / 10) * total_inheritance
                        if ibu > 0 or nenek > 0:
                            share_cp = (16/ 27) * total_inheritance

            if anak_perempuan == 1:               
                if (saudara_laki_kandung > 0 or saudara_perempuan_kandung > 0):
                    share_cp = (1 / 6) * total_inheritance
                if ayah == 0 and kakek == 0 and suami == 0 and istri == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                    if ibu > 0 or nenek > 0:
                        share_cp = (1 / 5) * total_inheritance
                if (ayah > 0 or kakek > 0) and suami == 0 and istri == 0:
                    if ibu == 0 and nenek == 0:
                        share_cp = (1 / 5) * total_inheritance
                    if ibu > 0 or nenek > 0:
                        share_cp = (1 / 6) * total_inheritance

                if suami > 0:
                    if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                        if ibu == 0 and nenek == 0:
                            share_cp = (3 / 16) * total_inheritance 
                        if ibu > 0 or nenek > 0:
                            share_cp = (2 / 13) * total_inheritance
                    if ayah > 0 or kakek > 0:
                        if ibu == 0 and nenek == 0:
                            share_cp = (2 / 13) * total_inheritance
                        if ibu > 0 or nenek > 0:
                             share_cp = (2 / 15) * total_inheritance

                if istri > 0:
                    if ayah == 0 and kakek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
                        if ibu == 0 and nenek == 0:
                            share_cp = (7 / 32) * total_inheritance 
                        if ibu > 0 or nenek > 0:
                            share_cp = (7 / 40) * total_inheritance
                    if ayah > 0 or kakek > 0:
                        if ibu == 0 and nenek == 0:
                            share_cp = (7 / 40) * total_inheritance
                        if ibu > 0 or nenek > 0:
                             share_cp = (4 / 27)* total_inheritance

            if anak_perempuan >= 2:
                if cucu_laki > 0:
                    share_cp = ((cucu_perempuan)/(cucu_perempuan + (2 * cucu_laki))) * (total_inheritance - (share_suami + share_istri + share_ap + share_ayah + share_ibu + share_kakek + share_nenek))
                if cucu_laki == 0:
                    share_cp = 0
        if cucu_laki > 0 and anak_perempuan > 0:
            share_cp = ((cucu_perempuan)/(cucu_perempuan + (2 * cucu_laki))) * (total_inheritance - (share_suami + share_istri + share_ap + share_ayah + share_ibu + share_kakek + share_nenek))    
    else:
        share_cp = 0
    return share_cp
        
def hitung_bagian_si(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, saudara_seibu, ayah, kakek, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_laki_kandung, saudara_perempuan_kandung):
    share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
    share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
    share_ibu = hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
    share_nenek = hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)

    if saudara_seibu > 0 and ayah == 0 and kakek == 0 and anak_laki == 0 and anak_perempuan == 0 and cucu_laki == 0 and cucu_perempuan == 0:
        if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and saudara_laki_kandung == 0 and saudara_perempuan_kandung == 0:
            share_si = total_inheritance 
        if suami > 0 or istri > 0 or ibu > 0 or nenek > 0:
            share_si = total_inheritance - (share_suami + share_istri + share_ibu + share_nenek) 

        if saudara_seibu == 1:
            if saudara_laki_kandung > 0:
                share_si = (1 / 6) * total_inheritance

            if saudara_laki_kandung == 0:
                if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and saudara_perempuan_kandung == 1:
                    share_si = (1 / 4) * total_inheritance
                if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and saudara_perempuan_kandung >= 2:
                    share_si = (1 / 5) * total_inheritance
                if suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung == 1:
                    share_si = (1 / 5) * total_inheritance
                if suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung >= 2:
                    share_si = (1 / 6) * total_inheritance

                if suami > 0:
                    if saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0:
                        share_si = (1 / 7) * total_inheritance
                    if saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0:
                        share_si = (1 / 8) * total_inheritance
                    if saudara_perempuan_kandung == 0 and ibu > 0 and nenek == 0:
                        share_si = (1 / 6) * total_inheritance
                    if saudara_perempuan_kandung == 0 and nenek > 0 and ibu == 0:
                        share_si = (1 / 4) * total_inheritance
                    if saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0):
                        share_si = (1 / 8) * total_inheritance
                    if saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0):
                        share_si = (1 / 9) * total_inheritance

                if istri > 0:
                    if saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0:
                        share_si = (3 / 16) * total_inheritance
                    if saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0:
                        share_si = (2 / 13) * total_inheritance
                    if saudara_perempuan_kandung == 0 and ibu > 0 and nenek == 0:
                        share_si = (1 / 4) * total_inheritance
                    if saudara_perempuan_kandung == 0 and nenek > 0 and ibu == 0:
                        share_si = (3 / 8) * total_inheritance
                    if saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0):
                        share_si = (2 / 13) * total_inheritance
                    if saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0):
                        share_si = (2 / 15) * total_inheritance

        if saudara_seibu >= 2:
            if saudara_laki_kandung > 0:
                share_si = (1 / 3) * total_inheritance

            if saudara_laki_kandung == 0:
                if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and saudara_perempuan_kandung == 1:
                    share_si = (2 / 5) * total_inheritance
                if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and saudara_perempuan_kandung >= 2:
                    share_si = (1 / 3) * total_inheritance
                if suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung == 1:
                    share_si = (1 / 3) * total_inheritance
                if suami == 0 and istri == 0 and (ibu > 0 or nenek > 0) and saudara_perempuan_kandung >= 2:
                    share_si = (2 / 7) * total_inheritance

                if suami > 0:
                    if saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0:
                        share_si = (2 / 8) * total_inheritance
                    if saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0:
                        share_si = (2 / 9) * total_inheritance
                    if saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0):
                        share_si = (2 / 9) * total_inheritance
                    if saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0):
                        share_si = (2 / 10) * total_inheritance

                if istri > 0:
                    if saudara_perempuan_kandung == 1 and ibu == 0 and nenek == 0:
                        share_si = (4 / 13) * total_inheritance
                    if saudara_perempuan_kandung >= 2 and ibu == 0 and nenek == 0:
                        share_si = (4 / 15) * total_inheritance
                    if saudara_perempuan_kandung == 1 and (ibu > 0 or nenek > 0):
                        share_si = (4 / 15) * total_inheritance
                    if saudara_perempuan_kandung >= 2 and (ibu > 0 or nenek > 0):
                        share_si = (4 / 17) * total_inheritance
    else:
        share_si = 0
    return share_si

def hitung_bagian_sdlk(total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, share_ap, share_cp, share_si, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, anak_laki, cucu_laki, ayah, kakek, suami, istri, ibu, nenek, anak_perempuan, cucu_perempuan):
    if saudara_laki_kandung > 0 and anak_laki == 0 and cucu_laki == 0 and ayah == 0 and kakek == 0:
        share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
        share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
        share_ap = hitung_bagian_anak_perempuan(anak_perempuan, anak_laki, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung)
        share_ibu = hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        share_nenek = hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        share_cp = hitung_bagian_cucu_perempuan(cucu_perempuan, cucu_laki, anak_laki, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek)
        share_si = hitung_bagian_si(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, saudara_seibu, ayah, kakek, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_laki_kandung, saudara_perempuan_kandung)

        sisa = total_inheritance - (share_suami + share_istri + share_ibu + share_nenek + share_ap + share_cp + share_si)

        if saudara_perempuan_kandung > 0:
            share_sdlk = ((2 * saudara_laki_kandung)/(saudara_perempuan_kandung + (2 * saudara_laki_kandung))) * sisa
        if saudara_perempuan_kandung == 0:
            if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and anak_perempuan == 0 and cucu_perempuan == 0 and saudara_seibu == 0:
                share_sdlk = total_inheritance
            else:
                share_sdlk = sisa
    else:
        share_sdlk = 0

    return share_sdlk

def hitung_bagian_sdpk(total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, share_ap, share_cp, share_si, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, anak_laki, cucu_laki, ayah, kakek, suami, istri, ibu, nenek, anak_perempuan, cucu_perempuan):
    if saudara_perempuan_kandung > 0 and anak_laki == 0 and cucu_laki == 0 and ayah == 0 and kakek == 0:
        share_suami = hitung_bagian_suami(suami, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, kakek, ibu, nenek, saudara_laki_kandung, saudara_seibu, saudara_perempuan_kandung, total_inheritance)
        share_istri = hitung_bagian_istri(istri, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance)
        share_ap = hitung_bagian_anak_perempuan(anak_perempuan, anak_laki, cucu_laki, cucu_perempuan, suami, istri, ayah, ibu, kakek, nenek, total_inheritance, share_suami, share_istri, share_ayah, share_ibu, share_kakek, share_nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung)
        share_ibu = hitung_bagian_ibu(ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        share_nenek = hitung_bagian_nenek(nenek, ibu, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ayah, kakek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri)
        share_cp = hitung_bagian_cucu_perempuan(cucu_perempuan, cucu_laki, anak_laki, anak_perempuan, suami, istri, ayah, ibu, kakek, nenek, saudara_seibu, saudara_laki_kandung, saudara_perempuan_kandung, total_inheritance, share_suami, share_istri, share_ap, share_ayah, share_ibu, share_kakek, share_nenek)
        share_si = hitung_bagian_si(total_inheritance, share_suami, share_istri, share_ibu, share_nenek, saudara_seibu, ayah, kakek, anak_laki, anak_perempuan, cucu_laki, cucu_perempuan, suami, istri, ibu, nenek, saudara_laki_kandung, saudara_perempuan_kandung)

        sisa = total_inheritance - (share_suami + share_istri + share_ibu + share_nenek + share_ap + share_cp + share_si)

        if saudara_laki_kandung > 0:
            share_sdpk = ((saudara_perempuan_kandung)/(saudara_perempuan_kandung + (2 * saudara_laki_kandung))) * sisa
        if saudara_laki_kandung == 0:
            if suami == 0 and istri == 0 and ibu == 0 and nenek == 0 and anak_perempuan == 0 and cucu_perempuan == 0 and saudara_seibu == 0:
                share_sdpk = total_inheritance
            else:
                share_sdpk = sisa
    else: 
        share_sdpk = 0

    return share_sdpk