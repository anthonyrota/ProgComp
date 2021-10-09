// Timer element for ProgComp SVG animations
// Geoff Whale  grw171@gmail.com

// manipulates simulation time in response to user input
// elements are
//      fixed slider range bar
//      slider
//      elapsed time in seconds text box
//      pause/resume button

// functions
//      initTiming() - called in svg 


var rootElement = document.getElementById('root');
var timeElement;
var timelineElement;
var sliderElement;
var timerOffset = 5;
var sliderScale = 0;    // px per second
var stopped = false;
var maxTime;


function initTiming() {
     console.log("initialising...");
     // rootElement.pauseAnimations();
     timeElement = document.getElementById('timetext');
     timelineElement = document.getElementById('timeline');
     sliderElement = document.getElementById('slider');
     var timer =  document.getElementById('timer');

     var params = document.getElementById('params');
     if (params != null) {
         maxTime = params.getAttribute('data-max-time');
         console.log("Set max time to " + maxTime);
         var tmax = document.getElementById('tmax');
         tmax.textContent = maxTime;

         sliderScale = timelineElement.getAttribute('width') / maxTime;

         // move the timer group
         var timer_x = params.getAttribute('data-timer-x');
         var timer_y = params.getAttribute('data-timer-y');
         if (timer_x == null) {
             timer_x = 5;
         }
         if (timer_y == null) {
             timer_y = 600;
         }

         timer.setAttribute('transform', "translate(" + timer_x + ", " + timer_y + ")");
         timerOffset = timer_x;
     }

     console.log(timer.getAttribute('transform')); 
     showTime(0);
     setTimeout(keepTime, get_delay());

     console.log("timeline width = " + timelineElement.getAttribute('width'));
}

// https://stackoverflow.com/questions/14036107/moving-a-group-of-svg-elements-on-mouse-click/14036803#14036803

function sliderClick(evt) {
    moveSlider(evt.clientX - timerOffset);
}

function moveSlider(offset) {
    sliderElement.setAttribute("x1", offset);
    sliderElement.setAttribute("x2", offset);

    // new time, nearest second
    var sync = Math.round(offset/sliderScale);
    showTime(sync);
    rootElement.setCurrentTime(sync);
}

// Update displayed time
function showTime(et) {
    var sec = Math.floor(et);   // show seconds as they tick over, round would be 0.5s early
    // mm:sds could be displayed instead
    timeElement.textContent = sec;
}

// Pointer click on the pause/resume button
function pause(evt) {
    var pausetext = document.getElementById('pausetext');

    stopped = ! stopped;
    if (stopped) {
        rootElement.pauseAnimations();
        pausetext.textContent = "Resume";
    } else {
        pausetext.textContent = "Pause";
        setTimeout(keepTime, get_delay());
        rootElement.unpauseAnimations();
    }
}

// Time keeping
// Display current time and move slider
var keepTime = function() {
    if (stopped) {
        return;
    }

    var et = rootElement.getCurrentTime();
    // showTime(et);
    if (et > maxTime) {
        pause();
        return;
    }

    moveSlider(sliderScale*et);
    setTimeout(keepTime, get_delay());
}

// How long in ms until the next second ticks over? Used to schedule keepTime accurately.
function get_delay() {
    var et = rootElement.getCurrentTime();
    var etFrac = 1 - (et - Math.floor(et));
    if (etFrac < 0.1) {     // arbitrary fraction, skip if too small
        etFrac++;
    }
    etFrac *= 1000;   // now ms
    // console.log("delay (ms): " + etFrac);
    return etFrac;
}










