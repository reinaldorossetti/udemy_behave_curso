
Vamos fazer exemplo pegando a propriedade e o atributo do elemento, além de validar se o mesmo está habilitado, visível e selecionado.

### Exemplo HTML:

```
<!DOCTYPE html>
<html>
<body>
<h1>Display Radio Buttons</h1>
<form action="/action_page.php">
  <p>Please select your favorite Web language:</p>
<input type="radio" id="html" name="fav_language" value="HTML">
<label for="html">HTML</label><br>
<input type="radio" id="css" name="fav_language" value="CSS">
<label for="css">CSS</label><br>
<input type="radio" id="javascript" name="fav_language" value="JavaScript">
<label for="javascript">JavaScript</label>
  <br>  
  <p>Please select your age:</p>
  <input type="radio" id="age1" name="age" value="30">
  <label for="age1">0 - 30</label><br>
  <input type="radio" id="age2" name="age" value="60">
  <label for="age2">31 - 60</label><br>  
  <input type="radio" id="age3" name="age" value="100">
  <label for="age3">61 - 100</label><br><br>
  <input type="submit" value="Submit">
</form>
</body>
</html>
```

### Exemplo Código:
```
driver = webdriver.Chrome()
driver.get("http://localhost:8083/html/radio_exemplo.html")
CSS = (By.ID, "css")
AGE3 = (By.ID, "age3")

elemento01 = driver.find_element(*CSS).click()
elemento02 = driver.find_element(*AGE3).click()

# Gets the given attribute or property of the element.
elemento01_apos = driver.find_element(*AGE3)
valor01 = elemento01_apos.get_attribute("value")
valor02 = elemento01_apos.get_attribute("id")
AGE_VALUE = (By.CSS_SELECTOR, "label[for="+valor02+"]")

print(valor01)
print(valor02)
# verifica se o elemento foi selecionado
print(elemento01_apos.is_selected())
print(elemento01_apos.is_displayed())
print(elemento01_apos.is_enabled())

elemento_label = driver.find_element(*AGE_VALUE)
valor03 = elemento_label.get_property("textContent")
print(valor03)
assert "61 - 100" == valor03
```
comando: get_property("nome_da_propriedade")  
Obtém a propriedade fornecida do elemento.  

### Exemplo abaixo pega a propriedade texto do elemento "61 - 100":  
```
valor03 = elemento_label.get_property("textContent")
print(valor03)
```
comando: get_attribute("nome_do_atributo")  
### Exemplo abaixo pega o atributo ID de uma elemento e passa o valor para montar outro elemento.  
```
valor02 = elemento01_apos.get_attribute("id")
AGE_VALUE = (By.CSS_SELECTOR, "label[for="+valor02+"]")
elemento_label = driver.find_element(*AGE_VALUE)
```

### verifica se o elemento foi selecionado  
```
print(elemento01_apos.is_selected())
```
### Verifica se o elemento esta visível na tela.  
```
print(elemento01_apos.is_displayed())
```
### Verifica se o elemento esta habilitado na tela, não exatamente visível.  
```
print(elemento01_apos.is_enabled())
```
