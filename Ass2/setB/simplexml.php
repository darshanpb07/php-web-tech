SET B 
Q1


<?php 
    $xml = simplexml_load_file("book.xml");
    echo "<pre>";
    print_r($xml);
    echo "</pre>";
    foreach ($xml->book as $book) 
    {
        echo "Book No : " . $book->bookno . "<br>";
        echo "Book Name : " . $book->bookname . "<br>";
        echo "Author Name: " . $book->authorname . "<br>";
        echo "Price : " . $book->price . "<br>";
        echo "Year : " . $book->year . "<br>";
        echo "<hr>";
    }
?>
