<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Index 3</title>
    <!-- CSS -->
    <link rel="stylesheet" href="estilos.css">
</head>

<body>
    
    <!-- HEADER -->
    <header>
        <h1>
            Hiperligações
        </h1>
    </header>
    

    <!-- NAV -->
    <?php require "nav.php"; ?>


    <!-- HIPERLIGAÇÕES -->
    <section>

        <article>
            <h3>
                Links para recursos que estão no servidor
            </h3>
            <a href="nova_pagina.php" target="_blank">Nova página</a>
            <a href="../aula045_hiperligacoes/outras_paginas/outra_pagina.php" target="_blank">Página dentro de pasta</a>
            <a href="../../Secao_02_html5_css3_nivel_1/exercicio_final/index.html" target="_blank">Página fora da pasta atual</a>
        </article>

    </section>
    
</body>

</html>