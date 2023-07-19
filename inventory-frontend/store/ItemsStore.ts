import { defineStore } from 'pinia'

export const useItemsStore = defineStore('items', {
  state: () => ({
    items: null,
    popup: {name:null},
    info: false,
  }),

  getters: {

  },

  actions: {
    async getItems(){
    const response = await fetch('http://127.0.0.1:8000/items/category')
    const results = await response.json()
    console.log(results)
    this.items = results
    return results
    },
   
  }
  
})


