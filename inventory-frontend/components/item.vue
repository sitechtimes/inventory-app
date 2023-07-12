<template>
  <div class="itemMain" ref="main">
    <div class="image" v-if="info">
      <img class="imageView" :src="image" :alt="name_id" />
    </div>
    <div class="name-avail">
      <div class="name text">{{ name }}</div>

      <div class="quantity smalltext">
        {{ quantity }}
        <span class="availY avail smalltext" v-if="quantity > 0">
          Available</span
        >
        <span class="availN avail smalltext" v-else> Available</span>
      </div>

      <button class="dropdown" @click="clicked"></button>
    </div>
  </div>
</template>

<style scoped>
.itemMain {
  min-height: 9rem;
  height: fit-content;
  flex-basis: 23%;
  max-width: 23%;
  background-color: var(--whitebg);
  display: flex;
  flex-direction: row;
  position: relative;
  margin: 1rem;
  margin-left: 2rem;
  border-radius: 0.5rem;
  border: solid 1px var(--darkgray);
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
  color: var(--darkgray);

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
  height: 8rem;
  width: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #b696db;
  position: relative;
  overflow: hidden;
}
.imageView {
  position: absolute;
  max-height: 80%;
  max-width: 80%;
  object-fit: scale-down;
  object-position: center;
}
.dropdown {
  visibility: hidden;
}
@media screen and (max-width: 1600px) {
  .itemMain {
    max-width: 30%;
    flex-basis: 30%;
  }
}
@media screen and (max-width: 1100px) {
  .itemMain {
    max-width: 45%;
    flex-basis: 45%;
  }
}
@media screen and (max-width: 760px) {
  .itemMain {
    max-width: 95%;
    flex-basis: 95%;
    border: none;
    margin-left: 0;
  }
  .name-avail {
    width: 98%;
  }
  .name {
    padding-right: 1rem;
  }

  .dropdown {
    visibility: visible;
    clip-path: polygon(50% 100%, 0 0, 100% 0);
    width: 0.7rem;
    height: 0.6rem;
    position: absolute;
    right: 1.5rem;
    bottom: 1rem;
    border: none;
    background-color: #fbf7e4;
    z-index: 1000;
  }
  .dropdown:hover {
    cursor: pointer;
    background-color: #dfdbd7;
    scale: 1.1;
  }
}
</style>

<script>
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
  },
  data() {
    return {
      info: false,
    };
  },
  methods: {
    clicked() {
      console.log("clicked");
      this.info = !this.info;
    },

    infoScreen() {
      if (window.matchMedia("(min-width: 575px)").matches) {
        this.info = true;
      } else {
        this.info = false;
      }
    },
  },
  mounted() {
    this.infoScreen();
  },
};
</script>
