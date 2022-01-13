#iterate through speeches, split the words and use syllable estimator on words

totalsyllables_byspeech=[]
syllables_i=0
for i in speech_table["speech"]:
    words=i.split()
    for j in words:
        syllables_i+=sy.estimate(j)
    totalsyllables_byspeech.append(syllables_i)


speech_table["speech_syllable_count"]=pd.series(totalsyllables_byspeech)


print(speech_table["speech_syllable_count"])

#doesn't work yet seems not fast enough
