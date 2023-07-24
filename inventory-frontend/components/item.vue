<template>
  <div class="itemMain mainSize" ref="main" @mousedown="clicked">
    <div class="image">
      <img class="imageView" :src="image" :alt="name_id" />
    </div>
    <div class="name-avail" ref="textbox">
      <div class="name text" ref="name">{{ name }}</div>

      <div class="quantity smalltext" ref="quant">
        {{ quantity }}
        <span class="availY avail smalltext" v-if="quantity > 0">
          Available</span
        >
        <span class="availN avail smalltext" v-else> Available</span>
      </div>
    </div>
  </div>
</template>

<style>
.itemMain {
  min-height: 9rem;
  height: fit-content;

  background-color: var(--whitebg);
  display: flex;
  flex-direction: row;
  position: relative;
  margin: 1rem;
  margin-left: 2rem;
  border-radius: 0.5rem;
  border: solid 1px var(--darkgray);
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
  padding-right: 2.5rem;
}
.name,
.quantity,
.updated {
  padding-left: 1.5rem;
}

.name {
  padding-top: 1.2rem;
  margin-bottom: 3.5rem;

  height: fit-content;
}
.quantity {
  color: var(--darkergray);

  height: 50%;

  min-height: 1.5rem;
  display: flex;
  flex-direction: row;
  margin-bottom: 0.75rem;
  justify-content: space-evenly;

  position: absolute;
  bottom: 0;
  height: fit-content;
  padding-top: 0.5rem;
  padding-bottom: 0.4rem;
}

.updated {
  padding-top: 0.2rem;
  padding-bottom: 0.3rem;
}

.availY {
  color: rgb(53, 199, 155);
}
.availN {
  color: rgb(255, 43, 106);
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
  max-height: 80%;
  max-width: 80%;
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
    flex-basis: 45%;
  }
  .infoFull {
    max-width: 100%;
    flex-basis: 100%;
    border: none;
    margin: 0;
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
    border: none;
    margin: 0;
    border-radius: 0;
  }
  .name-avail {
    width: 98%;
    justify-content: center;
  }
  .name {
    padding-right: 1rem;
    margin-bottom: 0;
  }
  .quantity {
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
</style>

<script>
import { useItemsStore } from "~/store/ItemsStore";

export default {
  name: "Item",
  props: {
    name: String,
    quantity: Number,
    description: String,
    updated: String,
    available: Boolean,
    image: String,
    name_id: String,
    category: String,
    vendor: String,
  },

  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {
    resizing() {
      if (this.store.info === true) {
        this.store.textbox.forEach((item) => {
          item.classList.add("info-name-avail");
        });
        this.store.name.forEach((item) => {
          item.classList.add("info-name");
        });
        this.store.quant.forEach((item) => {
          item.classList.add("info-quantity");
        });

        this.store.main.forEach((item) => {
          item.classList.remove("mainSize");
          item.classList.add("infoFull");
        });
        this.store.cat.forEach((item) => item.classList.add("info-cat"));
      } else {
        this.store.main.forEach((item) => {
          item.classList.add("mainSize");
          item.classList.remove("infoFull");
        });
        this.store.textbox.forEach((item) => {
          item.classList.remove("info-name-avail");
        });
        this.store.name.forEach((item) => {
          item.classList.remove("info-name");
        });
        this.store.quant.forEach((item) => {
          item.classList.remove("info-quantity");
        });
        this.store.cat.forEach((item) => item.classList.remove("info-cat"));
      }
    },
    clicked() {
      console.log("clicked");

      if (this.store.popup.name === this.name) {
        if (this.store.info === false) {
          this.store.$patch({ info: true });
        } else {
          this.store.$patch({ info: false });
        }
      } else {
        this.store.$patch({
          popup: {
            image: this.image,
            name: this.name,
            category: this.category,
            quantity: this.quantity,
            link: this.description,
            vendor: this.vendor,
            date: this.updated,
          },
        });
        this.store.$patch({ info: true });
      }
      this.resizing();
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
