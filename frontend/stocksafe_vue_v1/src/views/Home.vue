
<template>
  <div>
    <!-- Begin Page Content -->
    <div class="container-fluid">
      <!-- Page Heading -->
      <div
        class="d-sm-flex align-items-center justify-content-between mb-4"
      ></div>

      <!-- Content Row -->

      <div>
        <!-- Area Chart -->
        <div>
          <div class="card shadow mb-4">
            <!-- Card Header - Dropdown -->
            <div
              class="
                card-header
                py-3
                d-flex
                flex-row
                align-items-center
                justify-content-between
              "
              style="width: 100%"
            >
              <h6 class="m-0 font-weight-bold text-primary mr-2">
                Today's Stock
                <i class="bi bi-arrow-90deg-left"></i>
              </h6>
            </div>
            <!-- Card Body -->
            <div class="card-body">
              <div>
                <!-- <canvas id="myAreaChart"></canvas> -->
                <div>
                  <b-carousel
                    id="carousel-1"
                    v-model="slide"
                    :interval="4000"
                    controls
                    indicators
                    background="#ababab"
                    img-width="1024"
                    img-height="480"
                    style="text-shadow: 1px 1px 2px #333"
                    @sliding-start="onSlideStart"
                    @sliding-end="onSlideEnd"
                  >
                    <!-- Text slides with image -->
                    <b-carousel-slide
                      v-for="(item, index) in list1"
                      :key="index"
                      :caption="item.caption"
                      :text="item.text"
                      :img-src="item.src"
                    >
                      <h1>{{ item.head }}</h1></b-carousel-slide
                    >
                    <!-- Slides with img slot -->
                    <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->

                    <!-- Slide with blank fluid image to maintain slide aspect ratio -->
                    <b-carousel-slide
                      caption="Blank Image"
                      img-blank
                      img-alt="Blank image"
                    >
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                        Suspendisse eros felis, tincidunt a tincidunt eget,
                        convallis vel est. Ut pellentesque ut lacus vel
                        interdum.
                      </p>
                    </b-carousel-slide>
                  </b-carousel>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /.container-fluid -->
  </div>
  <!-- End of Main Content -->
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  created() {
    //this.openWindowPop();
  },
  data() {
    return {
      list1: [
        {
          caption: "caption1",
          text: "Nulla vitae elit libero, a pharetra augue mollis interdum.",
          src: "https://picsum.photos/1024/480/?image=52",
          head: "Hello world!",
        },
        {
          caption: "caption2",
          text: "hhhhhhum.",
          src: "https://picsum.photos/1024/480/?image=54",
          head: "Hello world!2",
        },
        {
          caption: "caption3",
          text: "aaaaaaaaanterdum.",
          src: "https://picsum.photos/1024/480/?image=58",
          head: "Hello world!3",
        },
        {
          caption: "Blank Image",
          text: "Nulla vitae elit libero, a pharetra augue mollis interdum.",
          src: "https://picsum.photos/1024/480/?image=58",
          head: "Hello world!3",
        },
      ],
      slide: 0,
      sliding: null,
      key1: "width : 20%",
    };
  },
  components: {},
  methods: {
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
    openWindowPop() {
      var options =
        "top=10, left=10, width=500, height=600, status=no, menubar=no, toolbar=no, resizable=no";
      window.open("/popup", "popup", options);
    },
  },
  mounted() {},
};
</script>

<style>
@import url("../css/sb-admin-2.css");
/* @import url("css/sb-admin-2.min.css"); */
</style>