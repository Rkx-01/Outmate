export interface BuyingSignal {
  type: string;
  description: string;
  score: number;
  timestamp: string;
}

export interface Persona {
  title: string;
  pain_point: string;
  hook: string;
  channel: "email" | "linkedin" | "call";
  message_angle: string;
}

export interface CompetitiveIntel {
  competitors: string[];
  displacement_angle: string;
  landmine_questions: string[];
}

export interface Company {
  name: string;
  industry: string;
  location?: string;       // legacy alias
  headquarters?: string;   // backend field name
  description?: string;
  website?: string;
  funding_round?: string;
  funding_amount?: number;
  funding_date?: string;
  employee_count?: number;
  tech_stack: string[];
  hiring_signals: string[];
  buying_signals: BuyingSignal[];
  buying_signal_score: number;
  icp_score: number;
  personas?: Persona[];
  recommended_sequence?: string[];
  competitive_intel?: CompetitiveIntel;
}

export interface AgentEvent {
  event_type: string;
  data: any;
}

export interface GlobalGTMStrategy {
  hooks: string[];
  angles: string[];
  email_snippets: string[];
}

export interface RunResult {
  session_id: string;
  query: string;
  plan?: any;
  results?: Company[];
  companies?: Company[];
  signals?: any[];
  gtm_strategy?: GlobalGTMStrategy;
  confidence: number;
  overall_confidence?: number;
  reasoning_trace: string[];
}

export interface AgentState {
  agent_name: string
  status: 'waiting' | 'running' | 'complete' | 'error'
  started_at?: number
  duration_ms?: number
  attempt?: number
  confidence?: number
  reasoning?: string
  error?: string
}

export interface PipelineStatus {
  run_id: string
  query: string
  total_agents: number
  started_at: number
  duration_ms?: number
  companies_found?: number
}