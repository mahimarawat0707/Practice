<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculator</title>
<style>
    #calculator{
    border: 1px solid rgb(187, 183, 183);
    border-radius: 15px;
    width: 200px;
    background-color: rgb(199, 236, 90);
  }

  #display{
    margin: 10px;
    width: 85%;
    font-size: 25px;
    border-radius: 15px;
    background-color: rgb(222, 223, 223);
  }

  .button-container{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
  }

  .button{
    width: 45px;
    height: 45px;
    margin: 3px;
    background-color: rgb(206, 230, 134);
    border-radius: 15px;
  }
  #display{
    text-align: right;
  }

</style>

</head>
<body>
  <div id="calculator">
    <input type="text" id="display" placeholder="0" readonly>
    <div class="button-container">
      <button class="button" onclick="">C</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '1'; document.querySelector('#display').value = currentDisplay;">1</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '2'; document.querySelector('#display').value = currentDisplay;">2</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '+'; document.querySelector('#display').value = currentDisplay;">+</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '3'; document.querySelector('#display').value = currentDisplay;">3</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '4'; document.querySelector('#display').value = currentDisplay;">4</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '-'; document.querySelector('#display').value = currentDisplay;">-</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '5'; document.querySelector('#display').value = currentDisplay;">5</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '6'; document.querySelector('#display').value = currentDisplay;">6</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '*'; document.querySelector('#display').value = currentDisplay;">*</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '7'; document.querySelector('#display').value = currentDisplay;">7</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '8'; document.querySelector('#display').value = currentDisplay;">8</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '/'; document.querySelector('#display').value = currentDisplay;">/</button>

      <button class="button" onclick="currentDisplay = eval(currentDisplay); document.querySelector('#display').value = currentDisplay;">=</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '9'; document.querySelector('#display').value = currentDisplay;">9</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '9'; document.querySelector('#display').value = currentDisplay;">0</button>

      <button class="button" onclick="currentDisplay = currentDisplay + '.'; document.querySelector('#display').value = currentDisplay;">.</button>
    </div>
  </div>
  

  <script>
    let currentDisplay = '';
    document.querySelector('#display').value = currentDisplay;
  </script>
</body>
</html>
