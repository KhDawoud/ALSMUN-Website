<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import GroupSection from "../../Components/GroupSection.svelte";
    import HeadShot from "../../Components/HeadShot.svelte";
    import OmarGabr from "../../../assets/AC/ICJ/Omar Gabr - ICJ chair.jpg"
    import LilyAmmar from "../../../assets/AC/ICJ/Lily Ammar - ICJ cochair.jpg"
    import JalilaAbulmagd from "../../../assets/AC/ICJ/Jalila Abulmagd- ICJ cochair.jpg"
</script>
  

    <NavBar />
    <header class="px-10">
        <h1 class=" text-4xl font-bold text-center mt-10"> The International Court Of Justice </h1>
        <hr class="mb-6 mt-4">  
    </header>
    <main class="space-y-4 p-8">
        <GroupSection link={null} noReadMe={true} header="Omar Gabr - President Of ICJ" text={null} image={OmarGabr} />
        <section class="space-x-0 space-y-2 md:grid md:grid-flow-col md:grid-cols-2 md:space-x-3 md:space-y-0">
            <HeadShot name="Lily Ammar" title="Co-President" image={LilyAmmar} quote="Hi everyone! My name is Lily I'm your ICJ co-chair for this year's ALSMUN I'm sure it will be nothing short of spectacular. I can't wait to see you all, and work with you all."/>
            <HeadShot name="Jalila AbulMagd" title="Co-President" image={JalilaAbulmagd} quote="Hi everyone! My name's Jalila and I specifically enjoy ICJ because I'm planning on pursuing a career in international relations. This is my first time chairing a committee and I'm really excited to see you all at the conference!"/>
        </section>
    </main>

    