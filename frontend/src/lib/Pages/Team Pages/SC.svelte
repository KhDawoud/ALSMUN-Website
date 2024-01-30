<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import NourEldinNassar from "../../../assets/AC/SC/Nour eldin - Chair SC.jpg"
    import AhmedFraige from "../../../assets/AC/SC/Ahmed Fraige - Security Council cochair.jpg"
  </script>

    <NavBar />
    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-10"> Security Council </h1>
        <hr class="mb-2 mt-4">  
    </header>
    <main class="md:grid md:grid-flow-col md:grid-cols-2 md:m-5 md:space-x-4 md:space-y-0 p-5 space-x-0 space-y-2">
        <HeadShot name="Nour Eldin Nassar" title="Chair of SC" image={NourEldinNassar} quote="Hey everyone, my name is Nour El Din Nassar and I'll be your chair for this year's Security council. I fell in love with MUN and especially the Security council because of the exhilarating debates and performances that delegates can have. This year's Security Council will be one to remember as I know that the delegates coming will be able to provide the committee with fruitful, smart, and interesting clauses and debate that will make this conference one to remember. I look forward to seeing all of you in this conference and hope that you'll enjoy it as much as we will."/>
        <HeadShot name="Ahmed Fraige" title="Co-Chair of SC" image={AhmedFraige} quote="Hey everyone! My name is Ahmed Fraige and I will be co-chairing ALSMUN's Security Council. I believe that it takes a special kind of delegate to thrive in SC, but I am sure that all of you can exceed our expectations. I am excited to hear all of your powerful speeches, clever questions, and even all your crazy takes."/>
    </main>
  
    