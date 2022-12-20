
<template>
  <div>
    <!-- Begin Page Content -->
    <div class="container-fluid">
      <!-- Page Heading -->
      <div class="d-sm-flex align-items-center justify-content-between mb-4">
        <h1 class="h3 mb-0 text-gray-800">
          {{ stockdetailinfo.stockName }}
          <b-icon
            v-if="!myStock_tag"
            class="mb-2 mx-1 staricon2"
            icon="bag"
            variant="secondary"
            @click="addMyStock()"
          ></b-icon>
          <b-icon
            v-else
            class="mb-2 mx-1 staricon2"
            icon="bag-fill"
            variant="info"
            @click="deleteMyStock()"
          ></b-icon>
          <b-icon
            v-if="!star_tag"
            class="mb-2 mx-1 staricon1"
            icon="star"
            variant="secondary"
            @click="addLikeStock()"
          ></b-icon>
          <b-icon
            v-else
            class="mb-2 mx-1 staricon2"
            icon="star-fill"
            variant="warning"
            @click="deleteLikeStock()"
          ></b-icon>
        </h1>
      </div>

      <!-- Content Row -->
      <div class="row">
        <!-- Earnings (Monthly) Card Example -->
        <div class="col-xl-3 col-md-6 mb-4">
          <div class="card border-left-primary shadow h-100 py-2">
            <div class="card-body">
              <div class="row no-gutters align-items-center">
                <div class="col mr-2">
                  <div
                    class="
                      text-xs
                      font-weight-bold
                      text-primary text-uppercase
                      mb-1
                    "
                  >
                    시장
                  </div>
                  <div
                    class="h5 mb-0 font-weight-bold text-gray-800 clickTag"
                    @click="
                      goStockList('stock_market', stockdetailinfo.stockMarket)
                    "
                  >
                    {{ stockdetailinfo.stockMarket }}
                  </div>
                </div>
                <div class="col-auto">
                  <i class="fas fa-calendar fa-2x text-gray-300"></i>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Earnings (Monthly) Card Example -->
        <div class="col-xl-3 col-md-6 mb-4">
          <div class="card border-left-success shadow h-100 py-2">
            <div class="card-body">
              <div class="row no-gutters align-items-center">
                <div class="col mr-2">
                  <div
                    class="
                      text-xs
                      font-weight-bold
                      text-success text-uppercase
                      mb-1
                    "
                  >
                    섹터
                  </div>
                  <div
                    class="h5 mb-0 font-weight-bold text-gray-800 clickTag"
                    @click="
                      goStockList('stock_sector', stockdetailinfo.stockSector)
                    "
                  >
                    {{ stockdetailinfo.stockSector }}
                  </div>
                </div>
                <div class="col-auto">
                  <i class="fas fa-dollar-sign fa-2x text-gray-300"></i>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Pending Requests Card Example -->
        <div class="col-xl-6 col-md-6 mb-4">
          <div class="card border-left-warning shadow h-100 py-2">
            <div class="card-body">
              <div class="row no-gutters align-items-center">
                <div class="col mr-2">
                  <div
                    class="
                      text-xs
                      font-weight-bold
                      text-warning text-uppercase
                      mb-1
                    "
                  >
                    산업
                  </div>
                  <div
                    class="h5 mb-0 font-weight-bold text-gray-800 clickTag"
                    @click="
                      goStockList(
                        'stock_industry',
                        stockdetailinfo.stockIndustry
                      )
                    "
                  >
                    {{ stockdetailinfo.stockIndustry }}
                  </div>
                </div>
                <div class="col-auto">
                  <i class="fas fa-comments fa-2x text-gray-300"></i>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Earnings (Monthly) Card Example -->
        <!-- <div class="col-xl-3 col-md-6 mb-4">
          <div class="card border-left-info shadow h-100 py-2">
            <div class="card-body">
              <div class="row no-gutters align-items-center">
                <div class="col mr-2">
                  <div
                    class="text-xs font-weight-bold text-info text-uppercase mb-1"
                  >
                    가격 예측
                  </div>
                  <div class="row no-gutters align-items-center">
                    <div class="col-auto">
                      <div class="h5 mb-0 mr-3 font-weight-bold text-gray-800">
                        40%
                      </div>
                    </div>
                    <div class="col">
                      <div class="progress progress-sm mr-2">
                        <div
                          class="progress-bar bg-info"
                          role="progressbar"
                          :style="stockForeignerPer"
                          aria-valuenow="50"
                          aria-valuemin="0"
                          aria-valuemax="100"
                        ></div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-auto">
                  <i class="fas fa-clipboard-list fa-2x text-gray-300"></i>
                </div>
              </div>
            </div>
          </div>
        </div> -->
      </div>
      <div class="row">
        <div class="col-xl-8 col-lg-7">
          <!-- 가격 Chart -->
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
              >
                <h6 class="m-0 font-weight-bold text-primary">
                  가격요약
                  <b-icon
                    class="staricon2"
                    icon="arrow-clockwise"
                    variant="secondary"
                    @click="getPrice()"
                    style="font-size: 21px"
                  ></b-icon>
                  <span class="text-gray-600 ml-1" style="font-size: 9pt"
                    >( {{ nowTime }} 갱신)</span
                  >
                </h6>
                <!-- <div>
                  <button class="btn btn-primary">새로고침</button>
                </div> -->
              </div>
              <!-- Card Body -->
              <div class="card-body">
                <div class="row">
                  <div class="col-4" style="text-align: center">
                    <div v-if="priceDiff > 0">
                      <div class="h1 font-weight-bold text-danger">
                        {{ priceData.now }}
                      </div>
                      <div class="h5 font-weight-bold text-danger">
                        ( + {{ priceDiff }} )
                      </div>
                    </div>
                    <div v-else>
                      <div class="h1 font-weight-bold text-primary">
                        {{ priceData.now }}
                      </div>
                      <div class="h5 font-weight-bold text-primary">
                        ( {{ priceDiff }} )
                      </div>
                    </div>
                  </div>

                  <div></div>
                  <div class="col-8">
                    <div class="row">
                      <div class="col-6 row">
                        <div
                          class="h5 font-weight-bold text-gray-800 mr-5"
                          style="margin-top: 5px"
                        >
                          고가
                        </div>
                        <div class="row" style="font-size: 15pt">
                          {{ priceData.high }}
                          <div
                            class="ml-2"
                            style="font-size: 5pt; margin-top: 10px"
                          >
                            ($)
                          </div>
                        </div>
                      </div>
                      <div class="col-6 row">
                        <div
                          class="h5 font-weight-bold text-gray-800 mr-5"
                          style="margin-top: 5px"
                        >
                          종가
                        </div>
                        <div class="row" style="font-size: 15pt">
                          {{ priceData.prevClose }}
                          <div
                            class="ml-2"
                            style="font-size: 5pt; margin-top: 10px"
                          >
                            ($)
                          </div>
                        </div>
                      </div>
                    </div>
                    <hr />
                    <div class="row">
                      <div class="col-6 row">
                        <div
                          class="h5 font-weight-bold text-gray-800 mr-5"
                          style="margin-top: 5px"
                        >
                          저가
                        </div>
                        <div class="row" style="font-size: 15pt">
                          {{ priceData.low }}
                          <div
                            class="ml-2"
                            style="font-size: 5pt; margin-top: 10px"
                          >
                            ($)
                          </div>
                        </div>
                      </div>
                      <div class="col-6 row">
                        <div
                          class="h5 font-weight-bold text-gray-800 mr-5"
                          style="margin-top: 5px"
                        >
                          시가
                        </div>
                        <div class="row" style="font-size: 15pt">
                          {{ priceData.open }}
                          <div
                            class="ml-2"
                            style="font-size: 5pt; margin-top: 10px"
                          >
                            ($)
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- 표 -->
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
              >
                <h6 class="m-0 font-weight-bold text-primary">
                  Earnings Overview
                </h6>
                <div class="dropdown no-arrow">
                  <b-icon
                    class="questionIcon"
                    icon="question-circle"
                    v-b-popover.hover.left="this.graphExplanation"
                  ></b-icon>
                </div>
              </div>
              <!-- Card Body -->
              <div class="card-body">
                <img :src="predictImgUrl" style="width: 100%; height: 100%" />
              </div>
            </div>
          </div>
        </div>

        <!-- 투자정보 -->
        <div class="col-xl-4 col-lg-5">
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
            >
              <h6 class="m-0 font-weight-bold text-primary">투자정보</h6>
            </div>
            <!-- Card Body -->
            <div class="card-body">
              <stock-table :priceData="priceData" />
            </div>
          </div>
        </div>
      </div>

      <!-- Content Row news -->
      <div class="row">
        <!-- Content Column -->
        <div class="col-lg-12 mb-4">
          <!-- Project Card Example -->
          <div class="card shadow mb-4">
            <div class="card-header py-3">
              <h6 class="m-0 font-weight-bold text-primary">뉴스</h6>
            </div>
            <div class="card-body">
              <list-table :data="newsData" type="two"> </list-table>
            </div>
          </div>
        </div>
      </div>
      <!-- news end-->

      <!-- Content Row Reply -->
      <div class="row">
        <!-- Content Column -->
        <div class="col-lg-12 mb-4">
          <!-- Project Card Example -->
          <div class="card shadow mb-4">
            <div class="card-header py-3">
              <h6 class="m-0 font-weight-bold text-primary">댓글</h6>
            </div>
            <div class="card-body">
              <div class="form-group">
                <textarea
                  class="form-control"
                  style="resize: none; width: 90%; float: left"
                  rows="3"
                  id="comment"
                  v-model="comment"
                ></textarea>
                <button
                  class="btn btn-primary"
                  style="width: 10%; height: 86px; float: left"
                  @click="addReply()"
                >
                  입력
                </button>
              </div>
              <list-table :data="replyData" type="two"> </list-table>
            </div>
          </div>
        </div>
      </div>
      <!-- Reply end-->
    </div>
    <!-- /.container-fluid -->
  </div>
  <!-- End of Main Content -->
</template>

<script>
import http from "@/utils/http-common.js";
import { mapMutations } from "vuex";
import { mapGetters } from "vuex";

import ListTable from "@/components/list/ListTable.vue";
import StockTable from "@/components/stock/StockTable.vue";
export default {
  created() {
    this.star_tag = false;
    console.log(this.$route.params.star_tag);
    if (this.$route.params.star_tag) {
      this.star_tag = true;
    }

    this.myStock_tag = false;
    console.log(this.$route.params.myStock_tag);
    if (this.$route.params.myStock_tag) {
      this.myStock_tag = true;
    }

    this.SET_FALSE_NOW_PAGE_STATE;

    this.getInfo();
  },
  name: "StockDetail",
  data() {
    return {
      star_tag: false,
      myStock_tag: false,
      newsData: [],
      replyData: [],
      stockdetailinfo: { stockName: "" },
      stockForeignerPer: "",
      comment: "",
      priceData: {},
      priceDiff: "",
      nowTime: "",
      predictImgUrl:
        "https://storage.cloud.google.com/stocksafe_storage/prophet/img/",
      graphExplanation:
        "Facebook의 시계열 예측모델 Prophet을 이용하여 앞으로 1년 동안의 예측 가격을 제공합니다. 초록색 꺽은선 차트를 통해 확인할 수 있습니다. 빨간색, 초록색 막대 그래프는 지금까지의 시가를 보여줍니다.",
      showExplainBox: false,
    };
  },
  components: { ListTable, StockTable },
  computed: {
    ...mapGetters(["getId"]),
  },
  methods: {
    ...mapMutations([
      "SET_FALSE_NOW_PAGE_STATE",
      "SET_INDEX_LIKE_STOCK",
      "SET_INDEX_MY_STOCK",
    ]),
    getInfo() {
      http
        .get(`/stock`, { params: { id: this.$route.params.id } })
        .then(({ data }) => {
          console.log(data);
          console.log(">>");
          this.stockdetailinfo = data;
          console.log(this.stockdetailinfo);
          //this.stockForeignerPer = "width: 40%";

          this.predictImgUrl =
            "https://storage.cloud.google.com/stocksafe_storage/prophet/img/";
          this.predictImgUrl += this.stockdetailinfo.id;
          this.predictImgUrl += ".png";
          this.getPrice();
          this.getNews();
          this.getReplys();
        });
    },
    getPrice() {
      let today = new Date();
      this.nowTime = today.toLocaleString();
      http
        .get(`/stock/price`, { params: { id: this.$route.params.id } })
        .then(({ data }) => {
          console.log(data);
          console.log(this.stockdetailinfo);
          this.priceData = data;

          this.priceDiff = this.priceData.now - this.priceData.prevClose;
          this.priceDiff = this.priceDiff.toLocaleString();

          this.priceData.open = this.priceData.open.toLocaleString();
          this.priceData.prevClose = this.priceData.prevClose.toLocaleString();
          this.priceData.now = this.priceData.now.toLocaleString();
          this.priceData.high = this.priceData.high.toLocaleString();
          this.priceData.low = this.priceData.low.toLocaleString();
          this.priceData.marketCap = this.priceData.marketCap.toLocaleString();
          this.priceData.sharesOutstanding =
            this.priceData.sharesOutstanding.toLocaleString();
          this.priceData.eps = this.priceData.eps.toLocaleString();
          this.priceData.pe = this.priceData.pe.toLocaleString();
          this.priceData.bps = this.priceData.bps.toLocaleString();
          this.priceData.annualYield =
            this.priceData.annualYield.toLocaleString();
        });
    },
    addLikeStock() {
      http
        .post(`/likestock`, {
          memberId: this.getId,
          predictId: this.stockdetailinfo.id,
        })
        .then(() => {
          this.star_tag = true;
          this.SET_INDEX_LIKE_STOCK(this.stockdetailinfo.id);
          alert("관심 주식에 등록되었습니다.");
        });
    },
    deleteLikeStock() {
      http
        .delete(`/likestock`, {
          params: {
            memberId: this.getId,
            predictId: this.stockdetailinfo.id,
          },
        })
        .then(() => {
          this.star_tag = false;
          this.SET_INDEX_LIKE_STOCK(this.stockdetailinfo.id);
          alert("관심 주식에서 삭제되었습니다.");
        });
    },
    getNews() {
      http
        .get(`/news`, { params: { stockId: this.stockdetailinfo.id } })
        .then(({ data }) => {
          this.newsData = data;
        });
    },
    getReplys() {
      http
        .get(`/reply`, { params: { stockId: this.stockdetailinfo.id } })
        .then(({ data }) => {
          this.replyData = data;
        });
    },
    addMyStock() {
      http
        .post(`/memberstock`, {
          memberId: this.getId,
          predictId: this.stockdetailinfo.id,
        })
        .then(() => {
          this.myStock_tag = true;
          this.SET_INDEX_MY_STOCK(this.stockdetailinfo.id);
          alert("내 주식에 등록되었습니다.");
        });
    },
    deleteMyStock() {
      http
        .delete(`/memberstock`, {
          params: {
            memberId: this.getId,
            predictId: this.stockdetailinfo.id,
          },
        })
        .then(() => {
          this.myStock_tag = false;
          this.SET_INDEX_MY_STOCK(this.stockdetailinfo.id);
          alert("내 주식에서 삭제되었습니다.");
        });
    },
    goStockList(searchListTag, keyword) {
      this.$router
        .push({
          name: "ListStock",
          query: {
            tag: searchListTag,
            keyword: keyword,
          },
        })
        .catch(() => {});
    },
    addReply() {
      // 대댓아닌 경우에 해당
      console.log(this.getId);
      console.log(this.comment);
      http
        .post("/reply", {
          memberId: this.getId,
          stockId: this.stockdetailinfo.id,
          replyContent: this.comment,
          replyLevel: 0,
        })
        .then(() => {
          this.comment = "";
          this.getReplys();
        });
    },
  },
  mounted() {},
  watch: {
    $route(to, from) {
      if (to.path !== from.path) {
        this.star_tag = false;
        console.log(this.$route.params.star_tag);
        if (this.$route.params.star_tag) {
          this.star_tag = true;
        }

        this.myStock_tag = false;
        console.log(this.$route.params.myStock_tag);
        if (this.$route.params.myStock_tag) {
          this.myStock_tag = true;
        }

        this.SET_FALSE_NOW_PAGE_STATE;
        this.getInfo();
      }
    },
  },
};
</script>

<style>
@import url("../css/sb-admin-2.css");
/* @import url("css/sb-admin-2.min.css"); */

.staricon1:hover {
  cursor: pointer;
}

.staricon2:hover {
  opacity: 50%;
  cursor: pointer;
}

.questionIcon:hover {
  cursor: pointer;
}

.clickTag:hover {
  cursor: pointer;
}
</style>