<?php

require 'db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $dia = $_POST['dia'];
    $horario = $_POST['horario'];

    $sql = 'INSERT INTO agendamentos (dia, horario) VALUES (?, ?)';

    try {
        $stmt = $conn->prepare($sql);
        $stmt->execute([$dia, $horario]);
        echo 'Agendamento realizado com sucesso!';
    } catch(PDOException $e) {
        echo 'Erro ao agendar: ' . $e->getMessage();
    }
}
