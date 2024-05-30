<template>
  <div class="itemMain mainSize" ref="main" @mousedown="clicked">
    <div class="image">
      <img class="imageView" :src="image" :alt="name_id" />
    </div>
    <div class="name-avail" ref="textbox">
      <div class="name subheading" ref="name">{{ name }}</div>

      <div
        class="quantityC text"
        ref="quant"
        :class="alert ? 'availN' : 'availY'"
      >
        Quantity: {{ quantity }}
      </div>
    </div>
  </div>
</template>

<style>
.itemMain {
  min-height: 12rem;
  background-color: var(--whitebg);
  display: flex;
  flex-direction: row;
  position: relative;
  margin: 1rem;
  margin-left: 2rem;
  border-radius: 0.5rem;
  border: var(--border);
  transition: all 0.2s;
}

.itemMain:hover {
  border-color: var(--darkergray);
  box-shadow: 0 0.25rem 5px var(--darkergray);
}

.mainSize {
  flex-basis: 23%;
  max-width: 23%;
}

.infoFull {
  flex-basis: 30%;
  max-width: 30%;
}

.name-avail {
  width: 70%;
  height: auto;
  display: flex;
  flex-direction: column;
}

.name,
.quantityC,
.updated {
  padding-left: 1.5rem;
}

.name {
  padding-top: 1.2rem;
  margin-top: 1rem;
  margin-bottom: 1.5rem;
  margin-right: 1rem;
  text-overflow: ellipsis;
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  height: 50%;
}

.quantityC {
  height: 50%;

  min-height: 1.5rem;
  display: flex;
  flex-direction: row;
  margin-bottom: 2rem;
  justify-content: space-evenly;

  position: absolute;
  bottom: 0%;
  height: fit-content;
  padding-top: 0.5rem;
  padding-bottom: 0.4rem;
}

.updated {
  padding-top: 0.2rem;
  padding-bottom: 0.3rem;
}

.availY {
  color: rgb(97, 194, 165);
}

.availN {
  color: rgb(201, 37, 86);
}

.avail {
  padding-left: 0.5rem;
}

.image {
  height: 9rem;
  width: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #b696db;

  overflow: hidden;
}

.imageView {
  display: block;
  max-height: 90%;
  max-width: 90%;
  margin-top: auto;
  object-fit: scale-down;
}

@media screen and (max-width: 1600px) {
  .mainSize {
    max-width: 30%;
    flex-basis: 30%;
  }

  .infoFull {
    max-width: 45%;
    flex-basis: 45%;
  }
}

@media screen and (max-width: 1100px) {
  .mainSize {
    max-width: 45%;
    height: 105px;
    flex-basis: 45%;
  }

  .infoFull {
    max-width: 100%;
    flex-basis: 100%;
    margin-top: 2px;
    border-radius: 0;
  }

  .infoFull:hover {
    border-color: none;
    box-shadow: none;
    background-color: var(--gray);
  }

  .info-name-avail {
    width: 98%;
    justify-content: center;
  }

  .info-name {
    padding-right: 1rem;
    margin-bottom: 0;
  }

  .info-quantity {
    padding-top: 1rem;
    position: inherit;
    justify-content: left;
  }
}

@media screen and (max-width: 760px) {
  .mainSize {
    max-width: 100%;
    flex-basis: 100%;
    margin-top: 2px;
    border-radius: 0;
  }

  .name-avail {
    width: 98%;
    justify-content: center;
  }

  .name {
    padding-right: 1rem;
    margin-bottom: 0;
    font-size: 11px;
    text-overflow: ellipsis;
  }

  .quantityC {
    padding-top: 1rem;
    position: inherit;
    justify-content: left;
  }

  .itemMain:hover {
    border-color: none;
    box-shadow: none;
    background-color: var(--gray);
  }
}

@media screen and (max-width: 375px) {
  .name {
    font-size: 13px;
    text-overflow: ellipsis;  
  }
}
</style>

<script>
import { useItemsStore } from "~/store/ItemsStore";

export default {
  name: "Item",
  props: {
    id: Number,
    name: String,
    quantity: Number,
    purchase_link: String,
    updated: String,
    alert: Boolean,
    image: String,
    name_id: String,
    category: String,
    vendor: String,
    makerspace: Number,
    backroom: Number,
  },

  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {
    clicked() {
      this.store.getLogs(this.name);
      if (this.store.popup.name === this.name) {
        if (this.store.info === false) {
          this.store.$patch({ info: true, viewNotif: false });
        } else {
          this.store.$patch({
            info: false,
            vendor: false,
            vendorHeader: false,
            categoryPop: false,
            categoryHeader: false,
            editform: false,
          });
        }
      } else {
        this.store.$patch({
          id: this.id,
          popup: {
            image: this.image,
            name: this.name,
            category: this.category,
            quantity: this.quantity,
            link: this.purchase_link,
            vendor: this.vendor,
            date: this.updated,
            makerspace: this.makerspace,
            backroom: this.backroom,
          },
          info: true,
          vendor: false,
          vendorHeader: false,
          categoryPop: false,
          categoryHeader: false,
          viewNotif: false,
          editform: false,
        })
      }
      if (this.store.dismiss === false) {
        this.store.NavMenu();
      }
      this.store.resizing();
    },
    push() {
      this.store.quant.push(this.$refs.quant);
      this.store.main.push(this.$refs.main);
      this.store.textbox.push(this.$refs.textbox);
      this.store.name.push(this.$refs.name);
    },
  },
  mounted() {
    this.push();
  },
};
</script>
