<script>
    import { tweened } from "svelte/motion";

    let expectedDate = new Date(2024,1,2,9)
    let now = new Date();
    let timeDiff = expectedDate.getTime()- now.getTime()
    $: daysLeft = tweened(Math.floor(timeDiff/(1000 * 3600 * 24)))
    $: hoursLeft = tweened(Math.floor((timeDiff%(1000 * 3600*24))/(1000*3600)))
    $: minutesLeft = tweened(Math.floor((timeDiff%(1000*3600))/(1000*60)))
    $: secondsLeft = tweened(Math.floor((timeDiff%(1000*60))/1000))

    setInterval(()=> {
        if (timeDiff > 0){
            timeDiff-=1000;
        }
    },1000)
</script>

<div class = "flex items-center justify-center h-auto">
    <p class ="text-gray-700 text-8xl font-semibold">
        {$daysLeft}<span class="text-red-600">:</span>{$hoursLeft}<span class="text-red-600">:</span>{$minutesLeft}<span class="text-red-600">:</span>{$secondsLeft}
    </p>
</div>