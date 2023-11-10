<script lang="ts">
    export let quote: string;
    export let name: string;
    export let image: string;
    export let title: string;
</script>

<div class="p-5 text-center border-2 rounded-xl">
    <header class="text-2xl font-bold mb-2"> {title}</header>
    <div class="flex items-center justify-center">
    <img src={image} alt="Mahmoud" class="object-cover rounded-full mb-4 h-48"/> 
    </div>
    <p class="font-semibold">{name}</p>
    <p class="italic font-serif">"{quote}"</p>
</div>