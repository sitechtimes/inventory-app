<template>
  <div class="itemMain" ref="main">
    <div class="name-avail">
      <div class="name">{{ name }} ({{ quantity }})</div>
      <div class="avail-updated">
        <div class="availability">
          <span class="availY" v-if="available">Currently Available</span>
          <span class="availN" v-else>Currently Unavailable</span>
        </div>
        <div class="updated">Last updated: {{ updated }}</div>
      </div>
      <button class="dropdown" @click="clicked"></button>
    </div>

    <div class="description" v-if="info">
      {{ description }}
    </div>
  </div>
</template>

<style scoped>
.itemMain {
  height: 7.5rem;
  width: 75vw;
  max-width: 35rem;
  border-radius: 2rem;
  background-color: rgb(68, 27, 88);
  display: flex;
  flex-direction: row;
  position: relative;
}
.name-avail {
  width: 40%;
  height: 100%;
  display: flex;
  flex-direction: column;
}
.name,
.availability,
.updated {
  padding-left: 1.5rem;
}

.name {
  padding-top: 1.2rem;
  font-size: 1.1rem;

  max-height: 6rem;
}

.avail-updated {
  height: 50%;

  min-height: 1.5rem;
  display: flex;
  flex-direction: column;
  margin-bottom: 0.75rem;
  justify-content: space-evenly;
  font-size: 0.8rem;
}
.availability {
  padding-top: 0.5rem;
  padding-bottom: 0.2rem;
}
.availY {
  color: rgb(126, 255, 216);
}
.availN {
  color: rgb(255, 66, 122);
}

.description {
  max-height: 100%;
  width: 60%;
  padding: 1.5rem;
  color: #b696db;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.4s;
}
.dropdown {
  visibility: hidden;
}
@media screen and (max-width: 575px) {
  .itemMain {
    flex-direction: column;
    height: fit-content;
    padding-bottom: 3.5rem;
  }
  .name-avail {
    width: 100%;
  }
  .name {
    font-size: 1.05rem;
    padding-right: 1rem;
  }
  .avail-updated {
    position: absolute;
    bottom: 0;
    height: fit-content;
    padding-top: 0.4rem;
  }
  .availability,
  .updated {
    font-size: 0.75rem;
  }
  .availability {
    padding-bottom: 0rem;
  }

  .updated {
    padding-top: 0.2rem;
    padding-bottom: 0.3rem;
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

  .description {
    width: 80%;
    padding-left: 1.5rem;
    padding-bottom: 0.5rem;
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
