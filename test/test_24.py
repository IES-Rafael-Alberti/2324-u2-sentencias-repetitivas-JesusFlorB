from src.ejercicio24 import es_primo

def test_es_primo():
    assert es_primo(2) == True
    assert es_primo(4) == False
    assert es_primo(11) == True
    assert es_primo(1) == False
    assert es_primo(29) == True
    assert es_primo(100) == False