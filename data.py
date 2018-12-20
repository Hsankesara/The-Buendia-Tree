def load_data(pyDatalog):
    #Generation 1
    gen1 = ["Jose Arcadio Buendia", "Ursula Iguaran"]
    pyDatalog.assert_fact('married', gen1[0], gen1[1])
    pyDatalog.assert_fact('cousin', gen1[0], gen1[1])
    pyDatalog.assert_fact('buendia_blood', gen1[0], True)
    pyDatalog.assert_fact('buendia_blood', gen1[1], True)
    pyDatalog.assert_fact('gender', gen1[0], 'Male')
    pyDatalog.assert_fact('gender', gen1[1], 'Female')

    # Generation 2
    gen2 = ["Colonel Aureliano Buendia", "Jose Arcadio Buendia (II)", "Amaranta Buendia", "Pilar Ternera", "Remedios Moscote", "Rebeca Buendia"]
    pyDatalog.assert_fact('parent', gen1[0], gen2[0])
    pyDatalog.assert_fact('parent', gen1[1], gen2[0])
    pyDatalog.assert_fact('parent', gen1[0], gen2[1])
    pyDatalog.assert_fact('parent', gen1[1], gen2[1])
    pyDatalog.assert_fact('parent', gen1[0], gen2[2])
    pyDatalog.assert_fact('parent', gen1[1], gen2[2])
    pyDatalog.assert_fact('gender', gen2[2], 'Female')
    pyDatalog.assert_fact('gender', gen2[0], 'Male')
    pyDatalog.assert_fact('gender', gen2[1], 'Male')
    pyDatalog.assert_fact('gender', gen2[3], 'Female')
    pyDatalog.assert_fact('gender', gen2[4], 'Female')
    pyDatalog.assert_fact('gender', gen2[5], 'Female')
    pyDatalog.assert_fact('buendia_blood', gen2[0], True)
    pyDatalog.assert_fact('buendia_blood', gen2[1], True)
    pyDatalog.assert_fact('buendia_blood', gen2[2], True)
    pyDatalog.assert_fact('buendia_blood', gen2[3], False)
    pyDatalog.assert_fact('buendia_blood', gen2[4], False)
    pyDatalog.assert_fact('buendia_blood', gen2[5], False)
    pyDatalog.assert_fact('buendia', gen2[0], True)
    pyDatalog.assert_fact('buendia', gen2[1], True)
    pyDatalog.assert_fact('buendia', gen2[2], True)
    pyDatalog.assert_fact('buendia', gen2[3], False)
    pyDatalog.assert_fact('buendia', gen2[4], True)
    pyDatalog.assert_fact('buendia', gen2[5], True)
    pyDatalog.assert_fact('married', gen2[0], gen2[4])
    pyDatalog.assert_fact('married', gen2[1], gen2[5])


    # Generation 3
    gen3 = ["The 17 Aurelianos", "Aureliano Jose Buendia", "Arcadio (Jose Arcadio III)", "Santa Sofia de la Piedad"]
    pyDatalog.assert_fact('parent', gen2[0], gen3[0])
    pyDatalog.assert_fact('parent', gen2[0], gen3[1])
    pyDatalog.assert_fact('parent', gen2[3], gen3[1])
    pyDatalog.assert_fact('parent', gen2[1], gen3[2])
    pyDatalog.assert_fact('parent', gen2[3], gen3[2])
    pyDatalog.assert_fact('gender', gen3[0], 'Male')
    pyDatalog.assert_fact('gender', gen3[1], 'Male')
    pyDatalog.assert_fact('gender', gen3[2], 'Male')
    pyDatalog.assert_fact('gender', gen3[3], 'Female')
    pyDatalog.assert_fact('buendia_blood', gen3[0], True)
    pyDatalog.assert_fact('buendia_blood', gen3[1], True)
    pyDatalog.assert_fact('buendia_blood', gen3[2], True)
    pyDatalog.assert_fact('buendia_blood', gen3[3], False)
    pyDatalog.assert_fact('buendia', gen3[0], True)
    pyDatalog.assert_fact('buendia', gen3[1], True)
    pyDatalog.assert_fact('buendia', gen3[2], True)
    pyDatalog.assert_fact('buendia', gen3[3], True)
    pyDatalog.assert_fact('married', gen3[2], gen3[3])

    # Generation 4
    gen4 = ["Remedios the Beauty", "Fernanda del Carpio", "Aureliano Segundo Buendia", "Jose Arcadio Segundo Buendia"]
    pyDatalog.assert_fact('parent', gen3[2], gen4[0])
    pyDatalog.assert_fact('parent', gen3[3], gen4[0])
    pyDatalog.assert_fact('parent', gen3[2], gen4[2])
    pyDatalog.assert_fact('parent', gen3[3], gen4[2])
    pyDatalog.assert_fact('parent', gen3[2], gen4[3])
    pyDatalog.assert_fact('parent', gen3[3], gen4[3])
    pyDatalog.assert_fact('gender', gen4[0], 'Female')
    pyDatalog.assert_fact('gender', gen4[1], 'Female')
    pyDatalog.assert_fact('gender', gen4[2], 'Male')
    pyDatalog.assert_fact('gender', gen4[3], 'Male')
    pyDatalog.assert_fact('buendia_blood', gen4[0], True)
    pyDatalog.assert_fact('buendia_blood', gen4[1], False)
    pyDatalog.assert_fact('buendia_blood', gen4[2], True)
    pyDatalog.assert_fact('buendia_blood', gen4[3], True)
    pyDatalog.assert_fact('buendia', gen4[0], True)
    pyDatalog.assert_fact('buendia', gen4[1], True)
    pyDatalog.assert_fact('buendia', gen4[2], True)
    pyDatalog.assert_fact('buendia', gen4[3], True)
    pyDatalog.assert_fact('married', gen4[2], gen4[1])

    gen5 = ['Jose Arcadio Buendia (IV)', 'Renata Remedios Buendia (Meme)', 'Mauricio Babilonia', 'Amaranta Ursula Buendia']
    pyDatalog.assert_fact('parent', gen4[2], gen5[0])
    pyDatalog.assert_fact('parent', gen4[1], gen5[0])
    pyDatalog.assert_fact('parent', gen4[2], gen5[1])
    pyDatalog.assert_fact('parent', gen4[1], gen5[1])
    pyDatalog.assert_fact('parent', gen4[2], gen5[3])
    pyDatalog.assert_fact('parent', gen4[1], gen5[3])
    pyDatalog.assert_fact('gender', gen5[0], 'Male')
    pyDatalog.assert_fact('gender', gen5[1], 'Female')
    pyDatalog.assert_fact('gender', gen5[2], 'Male')
    pyDatalog.assert_fact('gender', gen5[3], 'Female')
    pyDatalog.assert_fact('buendia_blood', gen5[0], True)
    pyDatalog.assert_fact('buendia_blood', gen5[1], True)
    pyDatalog.assert_fact('buendia_blood', gen5[2], False)
    pyDatalog.assert_fact('buendia_blood', gen5[3], True)
    pyDatalog.assert_fact('buendia', gen5[0], True)
    pyDatalog.assert_fact('buendia', gen5[1], True)
    pyDatalog.assert_fact('buendia', gen5[2], False)
    pyDatalog.assert_fact('buendia', gen5[3], True)

    gen6 = ['Aureliano (II)', 'Gaston']
    pyDatalog.assert_fact('parent', gen5[1], gen6[0])
    pyDatalog.assert_fact('parent', gen5[2], gen6[0])
    pyDatalog.assert_fact('gender', gen6[0], 'Male')
    pyDatalog.assert_fact('gender', gen6[1], 'Male')
    pyDatalog.assert_fact('buendia_blood', gen6[0], True)
    pyDatalog.assert_fact('buendia_blood', gen6[1], False)
    pyDatalog.assert_fact('buendia', gen6[0], True)
    pyDatalog.assert_fact('buendia', gen6[1], False)
    pyDatalog.assert_fact('married', gen6[1], gen5[3])

    gen7 = ['Aureliano (III)']
    pyDatalog.assert_fact('parent', gen6[0], gen7[0])
    pyDatalog.assert_fact('parent', gen5[3], gen7[0])
    pyDatalog.assert_fact('buendia_blood', gen7[0], True)
    pyDatalog.assert_fact('buendia', gen7[0], True)
    return