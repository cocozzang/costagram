<template>
  <div
    class="modal fade p-3"
    id="FeedModal"
    tabindex="-1"
    aria-labelledby="FeedModalLabel"
    aria-hidden="true"
  >
    <button
      type="button"
      class="btn-close float-end"
      data-bs-dismiss="modal"
      aria-label="Close"
    ></button>

    <div class="modal-dialog modal-xl mt-5">
      <div class="container-fluid">
        <div class="modal-content">
          <div class="row">
            <div class="col-8 p-0">
              <img src="@/assets/cat1.jpg" style="width: 100%" />
            </div>

            <div class="col-4 ps-0 pe-3">
              <div class="modal-header m-0 p-3">
                <div class="container p-0">
                  <div class="row justify-content-start">
                    <div class="col-2 ps-2">
                      <div
                        class="rounded-circle overflow-hidden d-flex justify-content-center align-items-center border me-3 feed-profile-photo"
                      >
                        <img
                          src="@/assets/cat1.jpg"
                          alt="photo"
                          style="
                            transform: scale(1.5);
                            width: 100%;
                            position: absolute;
                            left: 0;
                          "
                        />
                      </div>
                    </div>

                    <div class="col-6 p-0">
                      <div>
                        <span class="fw-bold" style="font-size: 80%">coco</span
                        ><span class="fw-bold" style="font-size: 80%">
                          • Following</span
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="modal-body m-0">
                <div class="container p-0">
                  <!-- feed description field start -->
                  <div class="row justify-content-start pb-2">
                    <div class="col-2 ps-2">
                      <div
                        class="rounded-circle overflow-hidden d-flex justify-content-center align-items-center border me-3 feed-profile-photo"
                      >
                        <img
                          src="@/assets/cat1.jpg"
                          alt="photo"
                          style="
                            transform: scale(1.5);
                            width: 100%;
                            position: absolute;
                            left: 0;
                          "
                        />
                      </div>
                    </div>

                    <div class="col-8 p-0">
                      <div>
                        <span style="font-size: 80%"
                          >nickname: description</span
                        >
                      </div>
                    </div>
                  </div>
                  <!-- feed description field end -->
                  <!-- feed comment field start -->
                  <div class="row justify-content-start pb-2">
                    <div class="col-2 ps-2">
                      <div
                        class="rounded-circle overflow-hidden d-flex justify-content-center align-items-center border me-3 feed-profile-photo"
                      >
                        <img
                          src="@/assets/cat1.jpg"
                          alt="photo"
                          style="
                            transform: scale(1.5);
                            width: 100%;
                            position: absolute;
                            left: 0;
                          "
                        />
                      </div>
                    </div>

                    <div class="col-8 p-0">
                      <div>
                        <span style="font-size: 80%">nickname : comment</span>
                      </div>
                    </div>
                  </div>
                  <!-- feed comment field end -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FeedModal",
  data() {
    return {
      props: {
        feedData: Object,
      },
    };
  },
};
</script>

<style></style>
