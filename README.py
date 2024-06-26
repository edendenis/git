#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `Git` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `Git` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and configurations for configuring/installing/use `Git` on `Linux Ubuntu`._
# 

# ## Descrição [2]
# 
# ### `Git`
# 
# O Git é um sistema de controle de versão distribuído amplamente utilizado para rastrear e gerenciar o código-fonte de projetos de desenvolvimento de software. Desenvolvido por Linus Torvalds, o criador do Linux, o Git é conhecido por sua eficiência, flexibilidade e capacidade de trabalhar tanto em projetos individuais quanto em equipes de desenvolvimento. Ele permite que os desenvolvedores acompanhem as alterações feitas no código, revertam para versões anteriores, colaborem em projetos e gerenciem conflitos de maneira eficaz. O Git também é suportado por várias plataformas de hospedagem de código, como o GitHub, o GitLab e o Bitbucket, o que o torna uma escolha central para o desenvolvimento colaborativo e a gestão de código-fonte em projetos de software.

# ## 1. Configurar/Instalar/Usar o `Git` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/Usar o `Git` no `Linux Ubuntu`, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# 3. Em seguida, você pode instalar o GeoGebra usando o comando apt. Execute o seguinte comando: `sudo apt install git-all -y`
# 
#     - O sistema irá solicitar sua senha de administrador. Digite-a e pressione Enter.
# 
# 4. O Ubuntu irá mostrar uma lista de pacotes a serem instalados e a quantidade de espaço em disco que eles ocuparão. Confirme a instalação digitando `Y` e pressionando `Enter`.
# 
#     - Aguarde enquanto o sistema baixa e instala o `Git` e suas dependências.
# 
# 5. Uma vez concluída a instalação, você pode iniciar o `Git` a partir do menu de aplicativos do Ubuntu ou digitandono terminal: `git --version`
# 
# Agora você deve ter o GeoGebra instalado e pronto para uso no seu sistema Ubuntu.

# ## 2. Código completo
# 
# Para instalar o `Git` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove
#     sudo apt update -y
#     sudo apt autoremove
#     sudo apt autoclean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install git-all -y
#     git --version
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instalação do git no linux.*** Disponivel em: <https://chat.openai.com/c/301d1a3d-627c-48ca-a6f0-151bcf1c0572> (texto adaptado). ChatGPT. Acessado em: 14/11/2023 23:13.
# 
# [2] OPENAI. ***VS code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 15/11/2023 16:47.
# 
