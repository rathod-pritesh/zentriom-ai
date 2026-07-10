<script>
	import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "$lib/components/ui/card/index.js";
	import { Button } from "$lib/components/ui/button/index.js";
	import { Input } from "$lib/components/ui/input/index.js";
	import { Badge } from "$lib/components/ui/badge/index.js";
	import { History, Search, Copy, Check, Sparkles, Languages, Share2, Code, Wrench, Briefcase } from "lucide-svelte";

	let searchQuery = $state("");
	let selectedFilter = $state("All");
	let copyId = $state(null);

	let items = $state([
		{ id: 1, type: "AI Chat", group: "Today", date: "2 hours ago", query: "Svelte 5 run-time optimization", result: "Examined reactive overhead in Svelte 5 ($state vs $derived) and proposed compiler optimization options.", icon: Sparkles, color: "text-[#A16207]", bg: "bg-[#A16207]/10" },
		{ id: 2, type: "Grammar Assistant", group: "Today", date: "5 hours ago", query: "Polished cover letter", result: "Corrected sentence: 'I have been writing code for 5 years and it has improved my work.'", icon: Languages, color: "text-[#C2410C]", bg: "bg-[#C2410C]/10" },
		{ id: 3, type: "LinkedIn Generator", group: "Yesterday", date: "Yesterday", query: "Svelte 5 runes post", result: "🚀 Thrilled to share my latest architecture strategy on designing scalable agentic AI frontends...", icon: Share2, color: "text-[#C2410C]", bg: "bg-[#C2410C]/10" },
		{ id: 4, type: "Bug Fix Assistant", group: "Yesterday", date: "Yesterday", query: "Express memory leak", result: "Added connection close handler on process terminate to resolve Express client timeouts.", icon: Wrench, color: "text-stone-700", bg: "bg-stone-100" },
		{ id: 5, type: "Code Explainer", group: "Last 7 Days", date: "4 days ago", query: "const double = (arr) => arr.map(x => x*2)", result: "This is a concise ES6 arrow function that doubles every item in a numeric array using maps.", icon: Code, color: "text-stone-600", bg: "bg-stone-100" },
		{ id: 6, type: "Job Discovery", group: "Last 7 Days", date: "5 days ago", query: "Senior Frontend jobs", result: "Matched 3 active Frontend developer vacancies in San Francisco area.", icon: Briefcase, color: "text-[#A16207]", bg: "bg-[#A16207]/10" }
	]);

	const filters = ["All", "AI Chat", "Grammar Assistant", "LinkedIn Generator", "Code Explainer", "Bug Fix Assistant", "Job Discovery"];
	const timeGroups = ["Today", "Yesterday", "Last 7 Days"];

	const filteredItems = $derived(
		items.filter(item => {
			const matchesSearch = item.query.toLowerCase().includes(searchQuery.toLowerCase()) || 
			                      item.result.toLowerCase().includes(searchQuery.toLowerCase());
			const matchesFilter = selectedFilter === "All" || item.type === selectedFilter;
			return matchesSearch && matchesFilter;
		})
	);

	function handleCopy(id, text) {
		navigator.clipboard.writeText(text);
		copyId = id;
		setTimeout(() => copyId = null, 1500);
	}
</script>

<div class="space-y-6">
	<!-- Filters Card -->
	<Card class="bg-white border-stone-200 shadow-xs">
		<CardContent class="p-4 flex flex-col gap-4">
			<div class="relative">
				<Search class="absolute left-3 top-3 size-4 text-stone-400 shrink-0" />
				<Input
					bind:value={searchQuery}
					placeholder="Search history content..."
					class="pl-9 bg-white border-stone-200 text-xs font-sans h-10"
				/>
			</div>
			<div class="flex flex-wrap gap-2">
				{#each filters as filter}
					<button
						onclick={() => selectedFilter = filter}
						class="px-3 py-1 rounded-full text-xs font-semibold select-none outline-none border transition-all cursor-pointer {selectedFilter === filter ? 'bg-[#A16207]/10 border-[#A16207] text-[#A16207]' : 'border-stone-200 text-stone-500 hover:bg-stone-50'}"
					>
						{filter}
					</button>
				{/each}
			</div>
		</CardContent>
	</Card>

	<!-- Grouped History list -->
	<div class="space-y-8">
		{#each timeGroups as group}
			{@const groupItems = filteredItems.filter(item => item.group === group)}
			{#if groupItems.length > 0}
				<div class="space-y-3">
					<h3 class="text-xs font-bold text-stone-400 font-sans uppercase tracking-wider pl-1">
						{group}
					</h3>
					<div class="space-y-4">
						{#each groupItems as item}
							<Card class="bg-white border-stone-200 shadow-xs">
								<CardContent class="p-5 flex items-start gap-4">
									<div class="p-2 rounded-lg {item.bg} {item.color} shrink-0 mt-0.5">
										<item.icon class="size-4 shrink-0" />
									</div>
									<div class="flex-1 min-w-0 space-y-2">
										<div class="flex justify-between items-start gap-4">
											<div class="flex items-center gap-2">
												<Badge variant="outline" class="text-[9px] font-sans text-stone-500 uppercase tracking-wider">{item.type}</Badge>
												<span class="text-[10px] text-stone-400 font-sans">{item.date}</span>
											</div>
											<Button onclick={() => handleCopy(item.id, item.result)} variant="outline" class="border-stone-200 hover:bg-stone-50 h-7 px-2.5 text-[10px] font-sans cursor-pointer">
												{#if copyId === item.id}
													<Check class="size-3 text-emerald-600 mr-1" /> Copied
												{:else}
													<Copy class="size-3 mr-1" /> Copy Result
												{/if}
											</Button>
										</div>
										<div class="text-xs font-sans leading-relaxed">
											<p class="font-bold text-stone-900">{item.query}</p>
											<p class="text-stone-500 mt-1 whitespace-pre-wrap">{item.result}</p>
										</div>
									</div>
								</CardContent>
							</Card>
						{/each}
					</div>
				</div>
			{/if}
		{/each}

		{#if filteredItems.length === 0}
			<div class="flex flex-col items-center justify-center p-8 text-center text-stone-400 bg-white border border-stone-200 rounded-xl min-h-[160px]">
				<History class="size-8 text-stone-300 mb-2" />
				<p class="text-xs font-sans">No matching history entries found.</p>
			</div>
		{/if}
	</div>
</div>
