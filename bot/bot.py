import discord
from discord import app_commands
from discord.ext import commands, tasks
import datetime
import time
import asyncio
import random

# --- CONFIGURAÇÕES TÉCNICAS ---
TOKEN = "SEU_TOKEN_AQUI"
COR_SISTEMA = 0x00FF00  # Verde Hacker
COR_ALERTA = 0xFF0000   # Vermelho Alerta
CANAL_LOGS_ID = 123456789012345678  # COLOQUE O ID DO CANAL DE LOGS AQUI

class AllSafeBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix="!", intents=intents)
        self.user_xp = {}  # Memória temporária de XP (Ideal usar Banco de Dados depois)
        self.start_time = datetime.datetime.now()

    async def setup_hook(self):
        await self.tree.sync()
        self.monitor_task.start()

    @tasks.loop(minutes=1)
    async def monitor_task(self):
        # Aqui você pode adicionar lógica para pingar seus sites de Node.js
        pass

bot = AllSafeBot()

# --- 1. SISTEMA DE CANAIS DINÂMICOS (VOICE MASTER) ---
@bot.event
async def on_voice_state_update(member, before, after):
    # Nome do canal gatilho para criar salas
    NOME_GATILHO = "➕ Criar Sala"
    
    # LOG DE ATIVIDADE CYBERPUNK
    log_channel = bot.get_channel(CANAL_LOGS_ID)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    # Ação: Entrou em um canal
    if after.channel:
        if log_channel:
            await log_channel.send(f"`[{timestamp}]` 📥 **{member.display_name}** conectou em `{after.channel.name}`")

        # Lógica de Criar Sala
        if NOME_GATILHO in after.channel.name:
            guild = member.guild
            category = after.channel.category
            
            # Criando o canal com estética institucional
            novo_nome = f"🎙️ INTERROGATÓRIO: {member.display_name.upper()}"
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(connect=True),
                member: discord.PermissionOverwrite(mute_members=True, move_members=True, manage_channels=True)
            }
            
            canal_personalizado = await guild.create_voice_channel(
                name=novo_nome, 
                category=category, 
                overwrites=overwrites
            )
            
            await member.move_to(canal_personalizado)

            # Loop para deletar quando ficar vazio
            while True:
                await asyncio.sleep(5)
                if len(canal_personalizado.members) == 0:
                    await canal_personalizado.delete()
                    if log_channel:
                        await log_channel.send(f"`[{timestamp}]` 🗑️ Canal temporário de **{member.display_name}** encerrado.")
                    break

    # Ação: Saiu de um canal
    if before.channel and not after.channel:
        if log_channel:
            await log_channel.send(f"`[{timestamp}]` 📤 **{member.display_name}** desconectou de `{before.channel.name}`")

# --- 2. SISTEMA DE REGISTRO E PATENTE (HARDCORE RP) ---
@bot.tree.command(name="identidade", description="Gera seu registro de cidadão/policial no servidor")
async def identidade(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📑 SISTEMA DE IDENTIFICAÇÃO - ALLSAFE",
        description="Dados processados diretamente da rede central.",
        color=COR_SISTEMA
    )
    
    status = random.choice(["ATIVO", "EM OPERAÇÃO", "SOB INVESTIGAÇÃO"])
    id_fake = random.randint(1000, 9999)
    
    embed.add_field(name="👤 NOME", value=f"`{interaction.user.display_name}`", inline=True)
    embed.add_field(name="🆔 REGISTRO GERAL", value=f"`MG-{id_fake}`", inline=True)
    embed.add_field(name="📊 STATUS CRIMINAL", value=f"`{status}`", inline=False)
    embed.add_field(name="⏳ TEMPO DE SERVIDOR", value=f"`{ (datetime.datetime.now() - interaction.user.joined_at).days } dias`", inline=True)
    
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.set_footer(text="Acesso criptografado via Terminal v2.4")
    
    await interaction.response.send_message(embed=embed)

# --- 3. MONITORAMENTO DE UPTIME (ESTILO HACKER) ---
@bot.tree.command(name="status", description="Verifica a integridade dos sistemas AllSafe")
async def status(interaction: discord.Interaction):
    uptime = datetime.datetime.now() - bot.start_time
    # Simulando monitoramento de sites que você desenvolveu
    sistemas = {
        "Database PCMG": "🟢 ONLINE",
        "API Federal": "🟢 ONLINE",
        "Site Monitoring": "🟢 ONLINE",
        "Node.js Backend": "🟡 LATÊNCIA ALTA"
    }
    
    msg = "**🛰️ RELATÓRIO DE INTEGRIDADE DOS SISTEMAS**\n"
    msg += f"Uptime do Bot: `{str(uptime).split('.')[0]}`\n"
    msg += "```diff\n"
    for nome, st in sistemas.items():
        if "ONLINE" in st:
            msg += f"+ {nome:18} {st}\n"
        else:
            msg += f"- {nome:18} {st}\n"
    msg += "```"
    
    await interaction.response.send_message(msg)

# --- 4. COMANDO DE ANÚNCIO INSTITUCIONAL (PARA ADMS) ---
@bot.tree.command(name="comunicado", description="Envia um anúncio formal com estética policial")
@app_commands.checks.has_permissions(administrator=True)
async def comunicado(interaction: discord.Interaction, titulo: str, mensagem: str):
    embed = discord.Embed(
        title=f"🚨 COMUNICADO OFICIAL: {titulo.upper()}",
        description=mensagem,
        color=COR_ALERTA,
        timestamp=datetime.datetime.now()
    )
    embed.set_author(name="COMANDO GERAL - ALLSAFE", icon_url=bot.user.display_avatar.url)
    embed.set_footer(text="Este é um aviso prioritário. Ignorar pode resultar em punição.")
    
    await interaction.channel.send(content="@everyone", embed=embed)
    await interaction.response.send_message("Comunicado enviado com sucesso!", ephemeral=True)

# --- 5. COMANDO DE LIMPEZA (FAXINA NO TERMINAL) ---
@bot.tree.command(name="clear", description="Limpa o histórico de logs do terminal (chat)")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, quantidade: int):
    await interaction.response.defer(ephemeral=True)
    deleted = await interaction.channel.purge(limit=quantidade)
    await interaction.followup.send(f"🧹 `{len(deleted)}` linhas de código/mensagens removidas do terminal.")

# --- EVENTO DE INICIALIZAÇÃO ---
@bot.event
async def on_ready():
    print(f"{'='*30}")
    print(f"SISTEMA ONLINE: {bot.user.name}")
    print(f"ID DO BOT: {bot.user.id}")
    print(f"ESTADO: PRONTO PARA OPERAÇÃO")
    print(f"{'='*30}")
    
    activity = discord.Activity(
        type=discord.ActivityType.watching, 
        name="a rede AllSafe"
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)

bot.run(TOKEN)