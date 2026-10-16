<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Home</title>
    <!-- CSS -->
    <link rel="stylesheet" href="estilos.css">
</head>

<body>
    
    <header>
        <h1>
            Como colocamos elementos semânticos lado a lado?
        </h1>
        <p>
            Tradicionalmente são colocados em <i>stack</i> vertical.
        </p>
    </header>

    <?php require 'nav.php'; ?>

    <article>
        <section class="bg-red">
            <h2>
                Conteúdo do elemento um
            </h2>
        </section>

        <section class="bg-blue">
            <h2>
                Conteúdo do elemento dois
            </h2>
        </section>
    </article>
    
</body>

</html>