<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>IA - Contato</title>
    <link rel="shortcut icon" href="../../imagens/logo_empresa.png" type="image/png">
    <!-- CSS -->
    <link rel="stylesheet" href="assets/css/estilos.css">
</head>

<body>
    
    <!-- CABEÇALHO -->
    <?php include "assets/blocos_paginas/header.php" ?>


    <!-- NAVEGAÇÃO -->
    <?php include "assets/blocos_paginas/nav.php" ?>


    <!-- CONTATOS -->
    <section class="container-contatos">
        <h2 class="text-center">
            Contate-nos
        </h2>
        <h3 class="text-center">
            Estamos disponíveis 24/7 para suporte.
        </h3>

        <article class="text-center">
            <img src="../../imagens/icon_phone.png" alt="Telefone">
            <a href="https://wa.me/5587981346719?text=Olá,%20preciso%20de%20suporte!" class="contatos" target="_blank">Whatsapp</a>
            <small>Entre 09h00 e 19h00.</small>
        </article>
        <article class="text-center margin-top-40">
            <img src="../../imagens/icon_email.png" alt="E-mail">
            <a href="mailto:erick_ferreira@outlook.com" class="contatos">erick_ferreira@outlook.com</a>
            <small>Respondemos a todos os e-mails no prazo de 12 horas.</small>
        </article>
    </section>


    <!-- VER SERVIÇOS OU CONTATOS -->
    <section class="container-servicos-contatos">
        <h2>
            Conheça nossos serviços.
        </h2>
        <div class="botoes-servicos-contatos">
            <a href="servicos.php">Serviços</a>
        </div>
    </section>


    <!-- FOOTER -->
    <?php include "assets/blocos_paginas/footer.php" ?>
    
</body>

</html>