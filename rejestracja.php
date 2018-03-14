
<h1>Rejestracja</h1>
<p>Przesłane dane</p>
<?php
  print_r($_GET);
  print_r($_POST);
 ?>


     <form name="formularz" id="formularz" method="POST" action="rejestracja.php">
       <table class="table">
         <tr>
           <td>

       <label for="Imię">Imię</label>
     </td>
     <td>
       <input type="text" name="imie" value="" placeholder="Imię">
     </td>
   </tr>
 <tr>
   <td>
     <label for="Nazwisko">Nazwisko</label>
   </td>
   <td>
     <input type="text" name="Nazwisko" value="" placeholder="Nazwisko">
   </td>
 </tr>

 </table>

 <label for="gender">Wybierz płeć:</label> <br>
 <input type="radio" name="gender" value="male" checked> Male<br>
   <input type="radio" name="gender" value="female"> Female<br>
   <input type="radio" name="gender" value="other"> Other<br>
     <br>

     <input type="checkbox" name="vehicle1" value="Bike"> I have a bike<br>
     <input type="checkbox" name="vehicle2" value="Car"> I have a car

     <select name="cars">
       <option value="volvo">Volvo</option>
       <option value="saab">Saab</option>
       <option value="fiat">Fiat</option>
       <option value="Audi">Audi</option>
     </select>

     <select name="cars" size="4" multiple>
       <option value="volvo">Volvo</option>
       <option value="saab">Saab</option>
       <option value="fiat">Fiat</option>
       <option value="audi">Audi</option>
     </select>

     <br>
     <textarea name="komentarz" rows="4" cols="80"></textarea>
     <input type="submit" name="zapisz" value="zapisz">
       <input type="reset" name="reset" value="reset">

     </form>

     <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>
   </body>
 </html>
