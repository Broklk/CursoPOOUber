<?php

require_once("car.php");
require_once("uberX.php");
require_once("account.php");

$uberX = new UberX("B6E-482", new Account("Luis Rueda", "70059584"),
"Suzuki", "Grand Nomade");
$uberX->printDataCar();

$UberPool = new UberPool("AN-1212", new Account("Karen Moril", "70313165"),
"Volkswagen", "Bettle");

?>