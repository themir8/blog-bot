package bot

import (
	"fmt"
	"log"
	"os"
	"time"

	"github.com/joho/godotenv"
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
	})

	if err != nil {
		log.Fatal(err)
		return
	}

	bot.Handle("/start", OnStart)
	bot.Handle(tele.OnText, handle_text)

	bot.Start()
}
func OnStart(c tele.Context) error {
	// chat := c.Sender()
	texts, err := Get_articles("1355389870")
	if err != nil {
		log.Fatalln(err)
		return err
	} else if err == nil && texts == nil {
		log.Fatalln("У этого ползователя нет блога")
		return err
	}
	// texts := text.(map[string]interface{})
	for i, article := range texts {
		// if err != nil {
		// 	panic(err)
		// }
		resp := article.(map[string]interface{})
		fmt.Println(i, resp["blog"])

	}
	blog, err := Get_blog_by_owner_id("1355389870")
	if err != nil {
		log.Fatalln(err)
		return err
	}
	fmt.Println(blog)

	return c.Send("<b>Hello</b>")
}

func handle_text(c tele.Context) error {
	chat := c.Sender()
	user := User{UserID: chat.ID, UserName: chat.Username, FirstName: chat.FirstName, LastName: chat.LastName, Phone: "998998141352"}
	// switch c. {
	// case condition:

	// }
	fmt.Println(user.CreateUser())
	// fmt.Println(chat)

	return c.Send("<b>Hello</b>")
}
