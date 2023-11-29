<!-- VideoPlayer.vue -->
<template>
  <div ref="videoContainer" class="video-container">
    <video
      ref="videoPlayer"
      class="video-js vjs-default-skin"
      controls
    >
      <!-- <source :src="videoSource" type="video/mp4" /> -->
      <track
        @cuechange="(s) => console.log(s.target.track.activeCues[0]?.text)"
        v-if="subtitleSource"
        :src="subtitleSource"
        kind="metadata"
        srclang="fa"
        label="Persian"
        default
      />
    </video>
    <div class="overlay-text" @click="myPrint">a;sldfkas;dlfkjas;dfljksdf</div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import videojs from "video.js";
import "video.js/dist/video-js.css";

export default defineComponent({
  props: {
    videoSource: {
      type: String,
      required: true,
    },
    subtitleSource: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      player: null as videojs.Player | null,
      isFullscreen: false,
    };
  },
  mounted() {
    onMounted(() => {
      console.log("mount called")
      this.initVideoPlayer();
    });
  },
  beforeUnmount() {
    if (this.player) {
      this.player.dispose();
    }
  },
  methods: {
    myPrint() {
      this.$refs.videoContainer.requestFullscreen();
      // if(this.$refs.videoContainer.requestFullscreen){

      // }
    },
    initVideoPlayer() {
      console.log("wtf")
      const options = {
        controls: true,
        fill: true,
        children: {
          controlBar: {
            fullscreenToggle: false,
          },
        },
        // Add more options as needed
      };
      if(this.$refs.videoPlayer){
        console.log("it exsit")
      } else {
        console.log("shiiit")
      }

      this.player = videojs(this.$refs.videoPlayer, options);

      this.player.src({ type: "video/mp4", src: this.videoSource });

      if (this.subtitleSource) {
        const track = document.createElement("track");
        track.src = this.subtitleSource;
        track.kind = "subtitles";
        track.srclang = "en";
        track.label = "English";
        track.default = true;
        this.$refs.videoPlayer.appendChild(track);
      }

      const fullscreenButton = this.player
        .getChild("ControlBar")
        .getChild("FullscreenToggle")
        .el();
      console.log(fullscreenButton);

      // Add a click event listener to the fullscreen button
      fullscreenButton.addEventListener("click", this.toggleFullscreen);

      // Add event listener for fullscreenchange event
      document.addEventListener(
        "fullscreenchange",
        this.handleFullscreenChange
      );
      document.addEventListener(
        "webkitfullscreenchange",
        this.handleFullscreenChange
      );
      document.addEventListener(
        "mozfullscreenchange",
        this.handleFullscreenChange
      );
      document.addEventListener(
        "MSFullscreenChange",
        this.handleFullscreenChange
      );

      // Add Video.js event listener for fullscreenchange event
      this.player.on("fullscreenchange", this.handleFullscreenChange);
    },
    toggleFullscreen() {
      if (!this.isFullscreen) {
        // Enter fullscreen
        if (this.$refs.videoContainer.requestFullscreen) {
          this.$refs.videoContainer.requestFullscreen();
        } else if (this.$refs.videoContainer.mozRequestFullScreen) {
          this.$refs.videoContainer.mozRequestFullScreen();
        } else if (this.$refs.videoContainer.webkitRequestFullscreen) {
          this.$refs.videoContainer.webkitRequestFullscreen();
        } else if (this.$refs.videoContainer.msRequestFullscreen) {
          this.$refs.videoContainer.msRequestFullscreen();
        }
      } else {
        // Exit fullscreen
        if (document.exitFullscreen) {
          document.exitFullscreen();
        } else if (document.mozCancelFullScreen) {
          document.mozCancelFullScreen();
        } else if (document.webkitExitFullscreen) {
          document.webkitExitFullscreen();
        } else if (document.msExitFullscreen) {
          document.msExitFullscreen();
        }
      }
    },
    handleFullscreenChange() {
      // Update the fullscreen state
      this.isFullscreen = !!(
        document.fullscreenElement ||
        document.webkitFullscreenElement ||
        document.mozFullScreenElement ||
        document.msFullscreenElement
      );
    },
  },
});
</script>

<style scoped>
.video-container {
  position: relative;
}

.overlay-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 24px;
  color: rgb(155, 63, 63);
  text-align: center;
  z-index: 2147483647;
}
</style>
