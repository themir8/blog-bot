package bot

import (
	"log"
	"os"
	"time"

	"github.com/joho/godotenv"
	hl "github.com/mirsaid-mirzohidov/blog-bot/bot/handlers"
	tele "gopkg.in/tucnak/telebot.v3"
)

// var bot *tele.Bot

func Bot_run() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal(err)
		return
	}
	bot, err := tele.NewBot(tele.Settings{
		Token:     os.Getenv("BOT_TOKEN"),
		Poller:    &tele.LongPoller{Timeout: 10 * time.Second},
		ParseMode: "html",
		Verbose:   true,
	})

	if err != nil {
		log.Fatal(err)
		return
	}

	bot.Handle("/start", hl.OnStart)
	bot.Handle(tele.OnText, hl.OnText)

	bot.Start()
}
