<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Página 3</title>
    <!-- CSS -->
    <link rel="stylesheet" href="estilos.css">
</head>

<body>
    
    <header>
        <h1>
            Como colocamos elementos semânticos lado a lado?
        </h1>
        <p>
            Agora já temos uma <i>stack</i> horizontal.
        </p>
    </header>

    <?php require 'nav.php'; ?>

    <article>
        <section class="bg-red float-left padding-20">
            <h2>
                Conteúdo do elemento um
            </h2>
        </section>

        <section class="bg-blue float-left padding-20">
            <h2>
                Conteúdo do elemento dois
            </h2>
        </section>
    </article>
    
</body>

</html>