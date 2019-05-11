urls = {
    'URL_LOGIN':'http://208.115.201.248/hiscononline/index.php',
    'URL_HISCON':'http://208.115.201.248/hiscononline/hiscon.php'
}

credenciais ={
    'usuario':'julio10',
    'senha':'123456'
}

xpaths = {
    'LOGIN_BOX_USUARIO':'//input[@name="usuario"]',
    'LOGIN_BOX_SENHA':'//input[@name="senha"]',
    'BTN_LOGIN':'//input[@value="Entrar"]',
    'BTN_SAIR':'//a[@href="logout.php"]',

    'HISCON_BOX_CPF':'//input[@name="nb"]',
    'HISCON_BTN_BUSCAR':'//form[@action="?consulta=hiscon#hiscon"]//button[@name="con"][text()="Buscar"]',

    'HISCON_TBL_SOLICITACOES':'//div[@class="dados"]//table//td//a[@id="_ver"]'
}
