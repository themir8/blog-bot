package main

import (
	"github.com/mirsaid-mirzohidov/blog-bot/bot"
	"github.com/mirsaid-mirzohidov/blog-bot/bot/models"
)

// type Result struct {
// 	ID   string `json:"id"`
// 	Name string `json:"name"`
// }

func main() {
	models.InitDB()
	bot.Bot_run()
}
