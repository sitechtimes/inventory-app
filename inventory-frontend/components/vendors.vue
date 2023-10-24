<template>
  <div class="container">
    <div class="header itemHeader subheading">Vendors</div>
    <div class="content">
      <div class="buttons">
        <button
          v-for="data in vendor"
          :key="data"
          class="vendor-container"
          @click="showChartfuc(data.itemsVendor)"
        >
          <h1 class="vendor-name subheading">{{ data.vendor_name }}</h1>
        </button>
      </div>
      <div class="info canvas" v-show="showInfo" id="canvas" ref="canvas">
        <div class="extraInfoPanel">
          <div class="canvas-cont">
            <div
              :class="{ 'chart-cont-big': minMax, 'chart-cont-small': !minMax }"
            >
              <canvas
                id="Vendor"
                style="height: 100%; max-width: 100%"
              ></canvas>
            </div>
            <div class="btn-cont">
              <button
                v-if="!minMax"
                @click="fullScreen()"
                class="maximize-button"
              >
                <font-awesome-icon :icon="['fas', 'maximize']" />
              </button>
            </div>

            <button class="minimize-button" v-if="minMax" @click="fullScreen()">
              <font-awesome-icon :icon="['fas', 'minimize']" />
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { Chart } from "chart.js/auto";
import { useItemsStore } from "~/store/ItemsStore";

let showChart = ref(false);
let vendor = ref([]);
let chart = ref();
let showInfo = ref(false); // Step 1
let minMax = ref(false);
let canvas = ref();
let store = useItemsStore();

onMounted(() => {
  fetch("http://127.0.0.1:8000/items/vendor/", {
    method: "GET",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
  })
    .then((response) => response.json())
    .then((data) => {
      vendor.value = data;
    });
});

const chartData = ref({
  labels: [],
  datasets: [
    {
      label: "Total Stock Available",
      data: [],
      fill: false,
      borderColor: "rgb(75, 192, 192)",
      backgroundColor: "rgb(75, 1, 192)",
      tension: 0.1,
    },
  ],
});

const chartOptions = ref({
  responsive: true,
  scales: {
    y: {
      beginAtZero: true,
    },
    x: {
      ticks: {
        autoSkip: true,
        maxRotation: 80,
        minRotation: 80,
        fontSize: 16,
      },
      beforeUpdate(axis) {
        const labels = axis.chart.data.labels;
        for (let i = 0; i < labels.length; i++) {
          const lbl = labels[i];
          if (typeof lbl === "string" && lbl.length > 10) {
            labels[i] = lbl.substring(0, 10) + "..."; // cutting
          }
        }
      },
    },
  },
  plugins: {
    legend: {
      labels: {
        font: {
          size: 14,
        },
      },
    },
  },
});

function createChart() {
  const ctx = document.getElementById("Vendor").getContext("2d");
  const chart1 = new Chart(ctx, {
    type: "bar",
    data: chartData.value,
    options: chartOptions.value,
  });
  chart = chart1;
}

function updateChart(tag, quantity) {
  chart.data.labels = tag;
  chart.data.datasets[0].data = quantity;
  chart.update();
}

const showChartfuc = (vendorItem) => {
  showInfo.value = true; // Step 3

  if (!showChart.value) {
    showChart.value = true;

    let labels = [];
    let quantity = [];
    vendorItem.forEach((item) => {
      labels.push(item.name);
      quantity.push(item.total);
    });
    createChart();
    updateChart(labels, quantity);
  } else if (showChart.value) {
    let labels = [];
    let quantity = [];
    vendorItem.forEach((item) => {
      labels.push(item.name);
      quantity.push(item.total);
    });
    updateChart(labels, quantity);
  }
  if (store.dismiss === false) {
    store.NavMenu();
  }
};

const fullScreen = () => {
  if (minMax.value) {
    minMax.value = false;
    canvas.value.classList.remove("fullScreen");
  } else if (!minMax.value) {
    minMax.value = true;
    canvas.value.classList.add("fullScreen");
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.header {
  text-align: center;
  font-size: 24px;
  padding: 20px;
}

.content {
  display: flex;
  flex-direction: row;
  padding-top: 3rem;
}

.buttons {
  flex: 1;
  margin-left: 5rem;
}

.info {
  flex: 1;
}

.bigdiv {
  display: flex;
  flex-flow: column nowrap;
}

.other-stuff {
  display: flex;
  flex-flow: row nowrap;
}

.chart-cont {
  height: 70rem;
  width: 70rem;
}

.vendors {
  display: flex;
  max-width: 60%;
  flex-flow: row wrap;
}

.vendor-container {
  border: var(--border);
  padding: 30px 55px 30px 55px;
  margin: 6px;
  width: 24rem;
  transition: all 0.2s;
  border-radius: 0.5rem;
}

.vendor-container:hover {
  background-color: var(--halflightgray);
  cursor: pointer;
}

.vendor-name {
  color: #333;
  font-size: 20px;
  margin: 0;
}

#Vendor {
height: 60rem !important;
width: 90rem !important;
}

.fullScreen {
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 0;
  margin: 0;
  z-index: 9999;
  background-color: white;
  overflow: auto;
}

.canvas-cont {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  margin: 2rem;
}

.maximize-button,
.minimize-button {
  background-color: #3498db;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.minimize-button {
  position: relative;
  left: 45%;
  width: 8rem;
  margin-top: 100px;
}

.maximize-button {
  width: 8rem;
}

.maximize-button:hover,
.minimize-button:hover {
  background-color: #2980b9;
}

.maximize-button:active,
.minimize-button:active {
  background-color: #1f639e;
}

.btn-cont {
  display: flex;
  justify-content: flex-end;
  padding: 5px;
}

.chart-cont-big { 
  height: 50rem;
  display: flex;
  justify-content: center;
}

@media only screen and (orientation: landscape){
  .minimize-button {
    left: 45%;
    margin-bottom: 10vh;
  }
  
}

@media only screen and (orientation: landscape) and (max-height: 768px)
{
  
  #Vendor {
    height: 55rem !important;
    width: 80rem !important;
  }
  .minimize-button {
    margin-top: 10vh;
  }
}

@media screen and ( max-width: 912px ) {
  #Vendor {
    height: 45rem !important;
    width: 60rem !important;
  }
}

@media screen and (max-width: 820px) {
  #Vendor {
  height: 60rem !important;
  width: 50rem !important;
}
.minimize-button {
  margin-top: 100px;
  left: 45%;
}
}

@media screen and (max-width: 760px) {
  .content {
    flex-direction: column-reverse;
  }
  .chart-cont-small,
  .canvas-cont {
    max-width: 95%;
    margin-bottom: 3rem;
  }
  .canvas-cont,
  .buttons,
  .chart-cont-small {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;
  }
  .chart-cont-big {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  #Vendor {
    margin-top: 100px;
  }

  .minimize-button {  
   position:relative;
   right: 0% ;
   left: 0% ;

  }
    .buttons {
    margin-left: 0;
  }
}

@media  only screen and (max-width: 540px) {
 #Vendor {
  width: 50rem !important;
 }
  
}

@media screen and (max-width: 414px)  { 
  .canvas-cont {
    margin-top: 100px;
  }
  #Vendor {
    height: 20rem !important;
    width: 35rem !important;
  }
  
}


@media screen and (max-width: 280px)  { 
  #Vendor {
    height: 40rem !important;
    width: 18rem !important;
  }
}
</style>
