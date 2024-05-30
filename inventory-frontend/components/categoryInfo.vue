<template>
  <div id="popUpPanel" class="popUpPanel vendorPanel">
    <div class="chart1-cont">
      <div>
        <canvas id="myChart1"></canvas>
      </div>
      <div class="btn-cont">
        <button class="maximize-button" @click="maximizeChart()">
          <font-awesome-icon :icon="['fas', 'maximize']" />
        </button>
      </div>
    </div>
    <div class="no-show" ref="chart2">
      <div class="chart2-cont">
        <canvas id="myChart2"></canvas>
      </div>
      <button class="minimize-button" @click="maximizeChart()">
        <font-awesome-icon :icon="['fas', 'minimize']" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { Chart } from "chart.js/auto";
import { getRelativePosition } from "chart.js/helpers";
import { useItemsStore } from "~/store/ItemsStore";

const props = defineProps(["categoryName"]);
const store = useItemsStore();

const isMaximized = ref(false);
const chart2 = ref();
let CategoryItem = ref([]);
let ItemCount = ref([]);
let dataArray = ref(null);

const maximizeChart = () => {
  isMaximized.value = !isMaximized.value;
  if (isMaximized.value) {
    chart2.value.classList.remove("no-show");
    chart2.value.classList.add("fullScreen");
  } else if (!isMaximized.value) {
    chart2.value.classList.add("no-show");
    chart2.value.classList.remove("fullScreen");
  }
};
const chartData = ref({
  labels: CategoryItem.value,
  datasets: [
    {
      label: "Total Stock Available",
      data: ItemCount.value,
      fill: false,
      borderColor: "rgb(75, 192, 192)",
      backgroundColor: "rgb(32, 116, 180)",
      tension: 0.1,
    },
  ],
});

const chartOptions = ref({
  responsive: true,
  events: ["click", "mousemove"],
  scales: {
    y: {
      beginAtZero: true,
    },
    x: {
      ticks: {
        autoSkip: true,
        maxRotation: 0,
        minRotation: 0,
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

const createChart = () => {
  const ctx1 = document.getElementById("myChart1").getContext("2d");

  const chart1 = new Chart(ctx1, {
    type: "bar",
    data: chartData.value,
    options: {
      ...chartOptions.value,
      onClick: (e) => {
        let smallChart = Chart.getChart("myChart1");
        const canvasPosition = getRelativePosition(e, smallChart);
        const dataX = smallChart.scales.x.getValueForPixel(canvasPosition.x);
        const arr = dataArray.value[dataX];
        const item = arr.itemsCategory[dataX];
        store.$patch({ dataObject: item });
      },
    },
  });
  const ctx2 = document.getElementById("myChart2").getContext("2d");

  const chart2 = new Chart(ctx2, {
    type: "bar",
    data: chartData.value,
    options: {
      ...chartOptions.value,
      onClick: (e) => {
        let smallChart = Chart.getChart("myChart2");
        const canvasPosition = getRelativePosition(e, smallChart);
        const dataX = smallChart.scales.x.getValueForPixel(canvasPosition.x);
        const arr = dataArray.value[dataX];
        const item = arr.itemsCategory[dataX];
        store.$patch({ dataObject: item });
      },
    },
  });
};

onMounted(() => {
  fetchData();
});

async function fetchData() {
  try {
    const config = useRuntimeConfig();
    const response = await fetch(
      `${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/category/`,
      {
        method: "GET",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
      }
    );

    const data = await response.json();
    const CategoryName = props.categoryName;
    data.forEach((category) => {
      if (CategoryName === category.category_name) {
        category.itemsCategory.forEach((item) => {
          CategoryItem.value.push(item.name);
          ItemCount.value.push(item.total);
        });
      }
    });
    dataArray.value = data;
    createChart();
  } catch (error) {
    console.log("Error fetching data:", error);
  }
}
</script>

<style scoped>
.popUpPanel {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.no-show {
  display: none;
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
}

#myChart {
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.chart2-cont {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

#myChart2 {
  height: 70rem !important;
    width: 90% !important;
  padding: 2vw;
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
  margin-top: 10px;
}

.maximize-button {
  width: 4rem;
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

@media screen and (orientation: landscape) {
  .fullScreen {
    overflow: auto;
  }

  .minimize-button {
    margin-bottom: 10px;
  }
}

@media screen and (orientation: landscape) and (max-height: 540px) {
  #myChart1 {
    position: relative;
    height: 25rem !important;
    width: 80% !important;
  }

  .minimize-button {
    left: 45%;
  }
  .maximize-button {
    position: relative;
    bottom: 60px;
    flex-direction: row;
  }

  .popUpPanel {
    overflow: auto;
  }
}

@media only screen and (orientation: landscape) and (max-height: 375px) {
  #myChart2 {
    height: 50rem !important;
  }
}

@media screen and (max-width: 912px) {
  #myChart2 {
    margin-top: 25%;
  }
}

@media screen and (max-width: 667px) {
  #myChart2 {
    height: 80% !important;
    width: 80% !important;
  }
}

@media screen and (max-width: 414px) {
  #myChart2 {
    height: 38rem !important;
    width: 38rem !important;
  }
}
@media screen and (max-width: 375px) {
  #myChart1 {
    height: 20rem !important;
    width: 35rem !important;
  }

  #myChart2 {
    height: 30rem !important;
    width: 35rem !important;
  }
}

@media screen and (max-width: 360px) {
  #myChart1 {
    width: 34rem !important;
  }
}

@media screen and (max-width: 280px) {
  #myChart1 {
    width: 25rem !important;
    height: 20rem !important;
  }

  #myChart2 {
    width: 30rem !important;
    height: 25rem !important;
  }
  .minimize-button {
    position: relative;
    left: 40%;
    width: 8rem;
  }
}
</style>
