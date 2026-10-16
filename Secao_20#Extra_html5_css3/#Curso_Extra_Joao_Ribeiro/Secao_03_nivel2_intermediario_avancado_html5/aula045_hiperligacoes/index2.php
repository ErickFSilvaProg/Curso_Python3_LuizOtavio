<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Index 2</title>
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
                Não irá funcionar, precisa do "https://
            </h3>
            <a href="www.google.com" target="_blank">Ir para o Google</a>

            <h3>
                Dessa forma irá funcioar
            </h3>
            <a href="http://google.com" target="_blank">Ir para o Google</a>
        </article>
        
        <article>
            <h3>
                Imagem ou documento de texto
            </h3>
            <a href="../arquivos/google_logo.png" target="_blank">Link para imagem</a>
            <a href="../arquivos/arquivo-texto.txt" target="_blank">Link para texto</a>
        </article>

        <article>
            <h3>
                Outros recursos
            </h3>
            <a href="../arquivos/tabela_eletricista.pdf" target="_blank">Link para PDF</a>
            <a href="../arquivos/Lorem ipsum.docx" target="_blank">Link para DOCX</a>
            <a href="../arquivos/tabela_eletricista.zip" target="_blank">Link para ZIP</a>
        </article>

        <article>
            <h3>
                Recurso inexistente
            </h3>
            <a href="../arquivos/inexistente.gost" target="_blank">Link para recurso inexistente</a>
        </article>
        
    </section>

</body>

</html>