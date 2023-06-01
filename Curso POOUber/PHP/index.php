<?php
require_once("Account.php");
require_once("Car.php");
require_once("UberX.php");
require_once("UberPool.php");

$UberX = new UberX("VRR567", new Account("Andres Herrera", "DER864"), "Chevrolet", "Spark");
$UberX->printDataCar();

$UberPool = new UberPool("GST678", new Account("Andrea Herrera", "TYH573"), "Dodge", "Chart");
$UberPool->printDataCar();
?>