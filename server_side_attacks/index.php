<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Simples em PHP</title>
</head>
<body>
    <h1>Bem-vindo à minha página em PHP!</h1>

    <?php
        // Exibe a data e hora atual usando PHP
        echo "<p>Hoje é " . date("d/m/Y") . " e a hora atual é " . date("H:i:s") . ".</p>";
        // Variável PHP para exibir uma mensagem
        $mensagem = "Esta é uma página simples criada em PHP.";
        echo "<p>$mensagem</p>";
    ?>

    <footer>
        <p>&copy; <?php echo date("Y"); ?> - Meu Site PHP</p>
    </footer>
</body>
</html>
