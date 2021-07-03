package models

import (
	"log"

	"github.com/prologic/bitcask"
)

func InitDB() {
	db, _ := bitcask.Open("./db")
	defer db.Close()
	db.Put([]byte("Hello"), []byte("World"))
	val, _ := db.Get([]byte("Hello"))
	log.Printf(string(val))
}
