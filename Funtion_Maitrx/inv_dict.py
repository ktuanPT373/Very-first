def inv_dict(d):
    return {b:a for a,b in d.items()}
print(inv_dict({'thank you':'merci','goodbye':'au revoir'}))